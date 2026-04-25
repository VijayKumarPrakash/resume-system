#!/usr/bin/env python3
"""
fetch_jd.py - Fetch job description from a URL using Playwright.
Falls back gracefully if the page is blocked or JS-gated.

Usage:
    python scripts/fetch_jd.py <URL>

Install dependencies:
    pip install playwright
    playwright install chromium
"""

import sys
import argparse
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def fetch_jd(url: str, timeout: int = 15000) -> str:
    """
    Fetch and extract job description text from a URL.
    Returns the extracted text or raises an exception with a clear message.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )
        page = context.new_page()

        try:
            page.goto(url, wait_until="networkidle", timeout=timeout)
        except PlaywrightTimeoutError:
            # Page loaded but network didn't fully settle - still try to extract
            pass

        # Wait a moment for any lazy-loaded content
        page.wait_for_timeout(2000)

        # Try to extract main content - prioritize job-specific containers
        selectors = [
            "main",
            "[class*='job-description']",
            "[class*='job_description']",
            "[class*='jobDescription']",
            "[class*='posting']",
            "[class*='content']",
            "article",
            "body",
        ]

        text = ""
        for selector in selectors:
            try:
                element = page.query_selector(selector)
                if element:
                    text = element.inner_text()
                    if len(text.strip()) > 200:  # Enough content to be meaningful
                        break
            except Exception:
                continue

        browser.close()

        if not text or len(text.strip()) < 100:
            raise ValueError(
                "Could not extract meaningful content from this page. "
                "The site may be blocking headless browsers (common with LinkedIn, Handshake). "
                "Please paste the JD text directly."
            )

        return text.strip()


def main():
    parser = argparse.ArgumentParser(description="Fetch job description from URL")
    parser.add_argument("url", help="URL of the job posting")
    parser.add_argument(
        "--timeout", type=int, default=15000, help="Page load timeout in ms (default: 15000)"
    )
    args = parser.parse_args()

    try:
        text = fetch_jd(args.url, timeout=args.timeout)
        print(text)
    except ValueError as e:
        print(f"FETCH_FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(
            f"FETCH_FAILED: Unexpected error: {e}\n"
            "Please paste the JD text directly.",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
