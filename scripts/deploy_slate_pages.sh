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
Usage: scripts/deploy_slate_pages.sh --deploy

Builds Slate and deploys the build directory to Cloudflare Pages.

Required for remote deploy:
  --deploy

Optional env:
  CLOUDFLARE_PAGES_PROJECT  default: besttime-docs-api
  CLOUDFLARE_PAGES_BRANCH   default: main
  CLOUDFLARE_ENV_FILE       default: /Users/mickvermaat/Github/howbusyco/.env
EOF
  exit 0
fi

load_cloudflare_env
export CLOUDFLARE_API_TOKEN="${CLOUDFLARE_API_TOKEN:-${CF_TOKEN_API:-}}"
export CLOUDFLARE_ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:-${CF_ACCOUNT_ID:-}}"

if [[ "${1:-}" != "--deploy" ]]; then
  echo "Refusing to deploy without explicit --deploy. Use --help for usage." >&2
  exit 2
fi

CLOUDFLARE_PAGES_PROJECT="${CLOUDFLARE_PAGES_PROJECT:-besttime-docs-api}"

if command -v docker >/dev/null 2>&1; then
  docker run --rm --name slate-docs-build \
    -v "$(pwd)/build:/srv/slate/build" \
    -v "$(pwd)/source:/srv/slate/source" \
    slatedocs/slate build
else
  bundle exec middleman build --clean
fi

npx wrangler pages deploy build \
  --project-name "$CLOUDFLARE_PAGES_PROJECT" \
  --branch "${CLOUDFLARE_PAGES_BRANCH:-main}"
