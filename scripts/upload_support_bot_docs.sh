#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

load_cloudflare_env() {
  local env_file="${CLOUDFLARE_ENV_FILE:-/Users/mickvermaat/Github/howbusyco/.env}"
  [[ -f "$env_file" ]] || return 0

  while IFS='=' read -r key value; do
    case "$key" in
      CLOUDFLARE_API_TOKEN|CLOUDFLARE_ACCOUNT_ID|CF_TOKEN_API|CF_ACCOUNT_ID)
        value="${value%$'\r'}"
        value="${value%\"}"
        value="${value#\"}"
        value="${value%\'}"
        value="${value#\'}"
        export "$key=$value"
        ;;
    esac
  done < "$env_file"
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  cat <<'EOF'
Usage: scripts/upload_support_bot_docs.sh --deploy

Builds the support-bot markdown and uploads it to Cloudflare R2.

Required for remote upload:
  --deploy

Optional env:
  SUPPORT_BOT_DOCS_OUTPUT   default: build/llm_besttime_email_tutorials_api_docs.md
  SUPPORT_BOT_R2_BUCKET     default: besttime
  SUPPORT_BOT_R2_KEY        default: llm_besttime_email_tutorials_api_docs.md
  SUPPORT_BOT_LIVE_URL      default: https://cdn.besttime.app/<key>
  CLOUDFLARE_ENV_FILE       default: /Users/mickvermaat/Github/howbusyco/.env
EOF
  exit 0
fi

load_cloudflare_env
export CLOUDFLARE_API_TOKEN="${CLOUDFLARE_API_TOKEN:-${CF_TOKEN_API:-}}"
export CLOUDFLARE_ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:-${CF_ACCOUNT_ID:-}}"

if [[ "${1:-}" != "--deploy" ]]; then
  echo "Refusing to upload without explicit --deploy. Use --help for usage." >&2
  exit 2
fi

OUTPUT="${SUPPORT_BOT_DOCS_OUTPUT:-build/llm_besttime_email_tutorials_api_docs.md}"
R2_BUCKET="${SUPPORT_BOT_R2_BUCKET:-besttime}"
R2_KEY="${SUPPORT_BOT_R2_KEY:-llm_besttime_email_tutorials_api_docs.md}"
LIVE_URL="${SUPPORT_BOT_LIVE_URL:-https://cdn.besttime.app/${R2_KEY}}"

python3 scripts/build_support_bot_docs.py --output "$OUTPUT"

npx wrangler r2 object put "${R2_BUCKET}/${R2_KEY}" \
  --remote \
  --file "$OUTPUT" \
  --content-type "text/markdown; charset=utf-8" \
  --cache-control "public, max-age=300"

python3 scripts/build_support_bot_docs.py \
  --output "$OUTPUT" \
  --compare-live \
  --live-url "$LIVE_URL" \
  --max-diff-lines 80
