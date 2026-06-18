#!/usr/bin/env python3
"""Compatibility wrapper for the support-bot docs builder.

Historically this file concatenated `source/includes/*.md` alphabetically into
`combined_documentation.md`. That was not reproducible with the public Slate
docs because Slate uses the include order from `source/index.html.md`.

Use `scripts/build_support_bot_docs.py` for the full support-bot markdown.
This wrapper keeps the old entry point available and writes the combined API
documentation body in Slate include order.
"""

from pathlib import Path

from scripts.build_support_bot_docs import (
    DEFAULT_SLATE_INCLUDES,
    DEFAULT_SLATE_INDEX,
    build_api_docs,
)


def main() -> int:
    output = Path("combined_documentation.md")
    api_docs = build_api_docs(DEFAULT_SLATE_INDEX, DEFAULT_SLATE_INCLUDES)
    output.write_text(api_docs, encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
