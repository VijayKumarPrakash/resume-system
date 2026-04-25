#!/usr/bin/env python3
"""
compile_resume.py - Compile a .tex file to PDF and save to the correct output location.

Usage:
    python scripts/compile_resume.py <tex_filepath> <company> [role_abbrev]

Example:
    python scripts/compile_resume.py /Users/vkp/Desktop/Resume/Ramp/tex_VKP_Ramp_DS_20260425.tex Ramp DS

Install dependencies:
    brew install --cask mactex   # or: brew install basictex
    (then restart terminal so pdflatex is on PATH)
"""

import sys
import os
import subprocess
import shutil
import argparse
from pathlib import Path

OUTPUT_ROOT = Path("/Users/vkp/Desktop/Resume")


def compile_resume(tex_path: Path, company: str) -> Path:
    """
    Compile a .tex file to PDF using pdflatex.
    Saves the PDF alongside the .tex file in the company folder.
    Returns the path to the generated PDF.
    """
    tex_path = Path(tex_path).resolve()

    if not tex_path.exists():
        raise FileNotFoundError(f"TeX file not found: {tex_path}")

    if not shutil.which("pdflatex"):
        raise EnvironmentError(
            "pdflatex not found. Install it with:\n"
            "  brew install --cask mactex\n"
            "or:\n"
            "  brew install basictex\n"
            "Then restart your terminal."
        )

    # Company output folder
    company_dir = OUTPUT_ROOT / company
    company_dir.mkdir(parents=True, exist_ok=True)

    # Run pdflatex twice (second pass resolves references)
    for i in range(2):
        result = subprocess.run(
            [
                "pdflatex",
                "-interaction=nonstopmode",
                "-output-directory", str(company_dir),
                str(tex_path),
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0 and i == 1:
            print("pdflatex stderr:", result.stderr[-2000:])  # Last 2000 chars
            raise RuntimeError(
                f"pdflatex failed with return code {result.returncode}.\n"
                "Check the .tex file for errors."
            )

    # Clean up auxiliary files
    stem = tex_path.stem
    for ext in [".aux", ".log", ".out"]:
        aux_file = company_dir / f"{stem}{ext}"
        if aux_file.exists():
            aux_file.unlink()

    # The PDF filename matches the tex filename but without "tex_" prefix
    pdf_name = stem.replace("tex_", "", 1) + ".pdf"
    pdf_path = company_dir / pdf_name

    # pdflatex names output after the stem of the input file
    generated_pdf = company_dir / f"{stem}.pdf"
    if generated_pdf.exists() and generated_pdf != pdf_path:
        generated_pdf.rename(pdf_path)

    return pdf_path


def main():
    parser = argparse.ArgumentParser(description="Compile LaTeX resume to PDF")
    parser.add_argument("tex_path", help="Path to the .tex file")
    parser.add_argument("company", help="Company name (used for output folder)")
    args = parser.parse_args()

    try:
        pdf_path = compile_resume(Path(args.tex_path), args.company)
        print(f"SUCCESS: PDF saved to {pdf_path}")
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    except EnvironmentError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
