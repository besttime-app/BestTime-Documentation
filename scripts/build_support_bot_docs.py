#!/usr/bin/env python3
"""Build the BestTime support-bot markdown from explicit source parts.

The public support Worker uses one large markdown file as its system prompt.
This script makes that file reproducible:

- support_bot/*.md provides the support-specific prompt, overrides, templates,
  examples, and appendices.
- source/index.html.md provides the Slate include order.
- source/includes/_*.md provides the API reference body.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import ssl
import sys
import urllib.request
import urllib.error
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUPPORT_DIR = REPO_ROOT / "support_bot"
DEFAULT_SLATE_INDEX = REPO_ROOT / "source" / "index.html.md"
DEFAULT_SLATE_INCLUDES = REPO_ROOT / "source" / "includes"
DEFAULT_OUTPUT = REPO_ROOT / "build" / "llm_besttime_email_tutorials_api_docs.md"
DEFAULT_LIVE_URL = "https://cdn.besttime.app/llm_besttime_email_tutorials_api_docs.md"

SUPPORT_PARTS = [
    "system_prompt.md",
    "important_overrides.md",
    "context_venue_filter.md",
    "email_templates_and_tutorials.md",
]

POST_API_PART = "post_api_appendix.md"

REQUIRED_ANCHORS = [
    "<SYSTEM PROMPT>",
    "</SYSTEM PROMPT>",
    "<Important things to take into account>",
    "</Important things to take into account>",
    "<CONTEXT>",
    "<EMAIL TEMPLATES and tutorials>",
    "</EMAIL TEMPLATES and tutorials>",
    "<API Documentation>",
    "</API Documentation>",
    "</CONTEXT>",
]


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def ensure_trailing_newline(text: str) -> str:
    return text if text.endswith("\n") else text + "\n"


def escape_markdown_for_prompt(content: str) -> str:
    """Preserve the legacy prompt-safe conversion used for Slate docs."""
    content = re.sub(r"^```(\w*)$", r"===\1", content, flags=re.MULTILINE)
    content = re.sub(r"^```$", "===", content, flags=re.MULTILINE)
    content = re.sub(r"(?<!`)(`)(?!`)", r"\\`", content)
    content = re.sub(r"\$", r"\\$", content)
    return content


def parse_slate_include_order(index_path: Path) -> list[str]:
    includes: list[str] = []
    in_includes = False

    for raw_line in index_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        if line == "includes:":
            in_includes = True
            continue

        if not in_includes:
            continue

        match = re.match(r"\s*-\s+([A-Za-z0-9_-]+)\s*$", line)
        if match:
            includes.append(match.group(1))
            continue

        if line and not line.startswith(" "):
            break

    if not includes:
        raise ValueError(f"No includes found in {index_path}")

    return includes


def build_api_docs(index_path: Path, includes_dir: Path) -> str:
    chunks = [
        "<API Documentation>\n",
        "BestTime.app API documentation source https://documentation.besttime.app\n",
    ]

    for include_name in parse_slate_include_order(index_path):
        include_path = includes_dir / f"_{include_name}.md"
        if not include_path.exists():
            raise FileNotFoundError(
                f"Slate include '{include_name}' from {index_path} not found at {include_path}"
            )

        content = normalize_newlines(include_path.read_text(encoding="utf-8"))
        chunks.append(f"\n\n<!-- Content from {include_path.name} -->\n\n")
        chunks.append(escape_markdown_for_prompt(content))

    chunks.append("\n\n</API Documentation>\n")
    return "".join(chunks)


def read_support_parts(support_dir: Path) -> list[str]:
    parts: list[str] = []
    for name in SUPPORT_PARTS:
        path = support_dir / name
        if not path.exists():
            raise FileNotFoundError(f"Missing support-bot source part: {path}")
        parts.append(ensure_trailing_newline(normalize_newlines(path.read_text(encoding="utf-8"))))
    return parts


def build_support_bot_markdown(
    support_dir: Path,
    index_path: Path,
    includes_dir: Path,
) -> str:
    chunks = read_support_parts(support_dir)
    chunks.append(ensure_trailing_newline(build_api_docs(index_path, includes_dir)))

    post_api_path = support_dir / POST_API_PART
    if not post_api_path.exists():
        raise FileNotFoundError(f"Missing support-bot post-API appendix: {post_api_path}")
    chunks.append(ensure_trailing_newline(normalize_newlines(post_api_path.read_text(encoding="utf-8"))))

    output = "\n".join(part.rstrip("\n") for part in chunks) + "\n"
    validate_output(output)
    return output


def validate_output(text: str) -> None:
    missing = [anchor for anchor in REQUIRED_ANCHORS if anchor not in text]
    if missing:
        raise ValueError(f"Generated support markdown missing anchors: {', '.join(missing)}")

    api_start = text.index("<API Documentation>")
    api_end = text.index("</API Documentation>")
    api_text = text[api_start:api_end]
    if "```" in api_text:
        raise ValueError("Generated API documentation still contains triple-backtick code fences")

    live_limit_index = api_text.find("live_limit")
    if live_limit_index >= 0 and api_text.rfind("<!--", 0, live_limit_index) < api_text.rfind("-->", 0, live_limit_index):
        raise ValueError("Venue Filter live_limit docs must stay commented out for support-bot output")


def extract_between(text: str, start: str, end: str, *, include_end: bool = True) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index)
    if include_end:
        end_index += len(end)
    return text[start_index:end_index].strip() + "\n"


def seed_support_parts(seed_path: Path, support_dir: Path) -> None:
    text = normalize_newlines(seed_path.read_text(encoding="utf-8"))
    api_start = text.index("<API Documentation>")
    api_end = text.index("</API Documentation>") + len("</API Documentation>")

    parts = {
        "system_prompt.md": extract_between(text, "<SYSTEM PROMPT>", "</SYSTEM PROMPT>"),
        "important_overrides.md": extract_between(
            text,
            "<Important things to take into account>",
            "</Important things to take into account>",
        ),
        "context_venue_filter.md": text[text.index("<CONTEXT>"):text.index("<EMAIL TEMPLATES and tutorials>")].strip() + "\n",
        "email_templates_and_tutorials.md": extract_between(
            text,
            "<EMAIL TEMPLATES and tutorials>",
            "</EMAIL TEMPLATES and tutorials>",
        ),
        POST_API_PART: text[api_end:].strip() + "\n",
    }

    support_dir.mkdir(parents=True, exist_ok=True)
    for name, content in parts.items():
        (support_dir / name).write_text(content, encoding="utf-8")
        print(f"Wrote {support_dir / name}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch_live(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 BestTimeDocsBuilder/1.0"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read()
    except urllib.error.URLError as exc:
        if not isinstance(exc.reason, ssl.SSLCertVerificationError):
            raise
        print("Warning: local Python CA verification failed; retrying public CDN comparison without certificate verification.", file=sys.stderr)
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(request, timeout=30, context=context) as response:
            return response.read()


def compare_with_live(generated_text: str, live_url: str, max_diff_lines: int) -> int:
    generated = generated_text.encode("utf-8")
    live = fetch_live(live_url)

    print(f"Generated bytes: {len(generated)}")
    print(f"Generated sha256: {sha256_bytes(generated)}")
    print(f"Live bytes: {len(live)}")
    print(f"Live sha256: {sha256_bytes(live)}")

    if generated == live:
        print("Generated output matches live CDN object.")
        return 0

    print("Generated output differs from live CDN object.")
    generated_lines = generated_text.splitlines()
    live_lines = live.decode("utf-8", errors="replace").splitlines()
    diff = difflib.unified_diff(
        live_lines,
        generated_lines,
        fromfile="live",
        tofile="generated",
        lineterm="",
        n=2,
    )
    for index, line in enumerate(diff):
        if index >= max_diff_lines:
            print(f"... diff truncated after {max_diff_lines} lines")
            break
        print(line)
    return 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--support-dir", type=Path, default=DEFAULT_SUPPORT_DIR)
    parser.add_argument("--slate-index", type=Path, default=DEFAULT_SLATE_INDEX)
    parser.add_argument("--includes-dir", type=Path, default=DEFAULT_SLATE_INCLUDES)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--seed-from", type=Path, help="Split an existing full support markdown file into support_bot parts")
    parser.add_argument("--compare-live", action="store_true", help="Compare generated output with the live CDN object")
    parser.add_argument("--live-url", default=DEFAULT_LIVE_URL)
    parser.add_argument("--max-diff-lines", type=int, default=120)
    args = parser.parse_args(argv)

    if args.seed_from:
        seed_support_parts(args.seed_from, args.support_dir)

    output_text = build_support_bot_markdown(args.support_dir, args.slate_index, args.includes_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output_text, encoding="utf-8")
    print(f"Wrote {args.output}")

    if args.compare_live:
        return compare_with_live(output_text, args.live_url, args.max_diff_lines)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
