# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

_Resume system for Vijay Kumar Prakash. Last updated: 2026-05-15._

---

## Architecture

Three source files drive everything:

- **`candidate.md`** — Primary source of truth for facts and metrics. Use judgment to frame experience in the most favorable light for each role — strong framing, transferable skill mapping, and presenting adjacent experience confidently are all acceptable. Never invent specific numbers, dates, or credentials that don't exist. Bullet text may be rephrased freely — verbatim phrasing is fine when it reads well, but rewriting for clarity, impact, or role fit is encouraged. Facts and metrics must remain accurate; prose is fair game.
- **`template.tex`** — LaTeX formatting skeleton (margins, fonts, section structure). Content is swapped in per-role.
- **`CLAUDE.md`** (this file) — candidate identity, confirmed metrics, role framing axes, formatting rules, and workflow.

Generated files go to `/Users/vkp/Desktop/Resume/FTE Apps/[Company]/` — never inside this repo.

---

## Scripts & Environment

Python 3.12 virtual environment at `.venv/`. Playwright is the only notable dependency (for headless JD fetching). All scripts live in `scripts/`.

**First-time setup** (if `.venv/` doesn't exist):
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install playwright
playwright install chromium
```

**Launch Claude from within the venv** (use `scripts/start.sh`):
```bash
bash scripts/start.sh
```

**Fetch a job description from a URL:**
```bash
python scripts/fetch_jd.py <URL>
# Optional: --timeout 20000   (ms, default 15000)
```
If the script exits with `FETCH_FAILED`, the page is JS-gated — stop and ask the user to paste the JD.

**Compile a `.tex` file to PDF:**
```bash
python scripts/compile_resume.py <path/to/tex_VKP_Company_Role_YYYYMMDD.tex> <Company>
```
`pdflatex` must be on `PATH` (install via `brew install --cask mactex` or `brew install basictex`, then restart terminal). The script runs `pdflatex` twice, cleans aux files, and renames the output by stripping the `tex_` prefix from the stem (e.g. `tex_VKP_Ramp_DS_20260425.tex` → `VKP_Ramp_DS_20260425.pdf`).

---

## Candidate Identity

- **Name:** Vijay Kumar Prakash
- **Email:** vkp@berkeley.edu
- **Phone:** +1 (510) 365-3885
- **GitHub:** https://github.com/VijayKumarPrakash
- **LinkedIn:** https://linkedin.com/in/vijay-kumar-prakash
- **GPA:** 3.88, displayed as **3.9** on all resumes
- **Graduation:** UC Berkeley MIMS, May 2026

---

## Facts & Fabrication Policy

All facts, metrics, and accomplishments are in `candidate.md` — never fabricate specific numbers, dates, or credentials beyond what is documented there.

---

## Formatting Rules (apply to every resume, no exceptions)

- Margins: **0.45in all sides**
- No page numbers: `\pagestyle{empty}`
- No em-dashes: single dashes only
- GPA displayed as **3.9**
- Font: 11pt default; drop to 10.5pt only if content spills to page 2
- Content must fill page comfortably — no spill, no significant whitespace at bottom
- Coursework line: pack as full as possible on one line without wrapping
- Teaching Assistant bullet: omit unless space allows and role is relevant
- Do NOT include "Finishing MIMS at UC Berkeley (May 2026)" in summary — redundant
- MongoDB listed explicitly in skills where relevant
- All resumes must be exactly one page
- Use `\textbf{}` sparingly — highlight only the most impactful metric or keyword in select bullets, not every bullet. In the summary, use it at most once on the single strongest signal. The goal is to reward skimming, not make every line look busy.
- Christ University: omit location — display as "Christ University" with no city

---

## Workflow Instructions

### When given a URL:
1. Run `python scripts/fetch_jd.py <URL>` to fetch the JD
2. If fetch fails (JS-gated, blocked, exits with `FETCH_FAILED`), stop and ask user to paste the JD
3. Never proceed with assumed JD content — always ask

### When given a JD:
1. Read `candidate.md` for all facts and experience
2. Use `template.tex` as the structural skeleton
3. Identify the role axis (see Role Axes below)
4. Tailor the resume — framing, bullet selection, skills section
5. Save `.tex` to: `/Users/vkp/Desktop/Resume/FTE Apps/[Company]/tex_VKP_[Company]_[Role]_[YYYYMMDD].tex`
6. Confirm `.tex` file location to user
7. **Do not compile to PDF unless the user explicitly asks**

### When asked to compile to PDF:
1. Run: `python scripts/compile_resume.py <path/to/tex_VKP_Company_Role_YYYYMMDD.tex> <Company>`
2. PDF will be saved to: `/Users/vkp/Desktop/Resume/[Company]/VKP_[Company]_[Role]_[YYYYMMDD].pdf`
3. Confirm PDF file location to user

### Naming convention:
- `.tex`: `tex_VKP_[Company]_[Role]_[YYYYMMDD].tex`
- `.pdf`: `VKP_[Company]_[Role]_[YYYYMMDD].pdf`
- Role abbreviations: SWE, FDE, DS, PM, MLE, AE, SE, ANALYST, OTHER
- Auto-detect role from JD; confirm with user if ambiguous

### When asked to update a resume:
1. Read the existing `.tex` file
2. Make the requested change using str_replace
3. Confirm updated `.tex` file location
4. Do not recompile to PDF unless the user explicitly asks

### When asked to remember something permanently:
- Update this file (CLAUDE.md) or candidate.md as appropriate
- Never rely on conversation memory across sessions

---

## Role Axes & Framing Principles

- **FDE roles:** Lead with Mon Ami embedded customer work + D.E. Shaw compliance/financial context
- **AI Engineer roles:** LLM benchmark project is hero; frame around eval reliability, tool-calling, agent failure modes
- **Data/Analytics roles:** D.E. Shaw pipeline + Mon Ami BigQuery funnels; Oorvani for narrative communication
- **Backend/SWE roles:** D.E. Shaw distributed systems, data integrity story, CI/CD ownership
- **PM/Product roles:** Mon Ami high-autonomy PM work alongside senior PMs; Mon Ami PostHog analytics → roadmap decision
- **New grad roles:** Projects lead over experience; Berkeley framing as "graduating May 2026"
- **Founding/startup roles:** "Engineer who ships," Claude Code daily usage, founder ambition, fast feedback loops
- **ML/Research roles:** LLM benchmark project leads; PyTorch, HuggingFace, experimental design framing

---

## Standing Rules

- Never add specific numbers, timeframes, or technical details not in candidate.md
- Ask before inventing any new credential or experience
- GitHub always links to https://github.com/VijayKumarPrakash
- Oorvani Foundation: include for analytics, FDE, data storytelling roles; omit for pure SWE
- Cybersecurity Clinic (INFO 289): include for security-adjacent roles or where customer advisory is key
- TA bullet: omit unless space allows
- Cal Habitat for Humanity (Volunteering): include only when community impact, non-profit work, or social good is relevant to the role; omit by default
- Excel/Google Sheets: include in skills only when the JD explicitly mentions them; omit by default as they are not a differentiator for most roles
- If page spills: first tighten spacing, then drop Oorvani, then condense lower D.E. Shaw tiers
- If significant whitespace at bottom: restore content, loosen spacing, or add Oorvani back
