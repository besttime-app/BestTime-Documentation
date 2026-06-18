# Support Bot Knowledge Source

These files are the editable source parts for the public BestTime AI support
bot markdown.

Build the final markdown with:

```bash
python3 scripts/build_support_bot_docs.py
```

The generated file is written to:

```text
build/llm_besttime_email_tutorials_api_docs.md
```

## Source Order

The builder concatenates these support-specific files:

1. `system_prompt.md`
2. `important_overrides.md`
3. `context_venue_filter.md`
4. `email_templates_and_tutorials.md`

Then it generates the `<API Documentation>` section from the Slate source in
the exact include order from `source/index.html.md`.

Finally, it appends:

5. `post_api_appendix.md`

## Deploy

Upload the generated support-bot markdown to Cloudflare R2:

```bash
SUPPORT_BOT_R2_BUCKET=besttime scripts/upload_support_bot_docs.sh --deploy
```

The script uses `wrangler r2 object put`, so `CLOUDFLARE_API_TOKEN` and
`CLOUDFLARE_ACCOUNT_ID` must be available. The wrapper safely loads them from
`/Users/mickvermaat/Github/howbusyco/.env` by default, or from
`CLOUDFLARE_ENV_FILE` when set.

Deploy the public Slate docs to Cloudflare Pages:

```bash
scripts/deploy_slate_pages.sh --deploy
```

The default Pages project is `besttime-docs-api`, which serves
`documentation.besttime.app`.

## Notes

- Do not manually edit `build/llm_besttime_email_tutorials_api_docs.md`.
- Keep prompt behavior and support policies in this folder.
- Keep endpoint reference docs in `source/includes`.
- The builder escapes Slate markdown for prompt safety by replacing triple
  backtick code fences with `===` fences and escaping inline backticks and
  dollar signs.
