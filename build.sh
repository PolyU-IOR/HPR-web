#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SITE="$ROOT/site"
DOCS="$ROOT/docs"
LANDING="$ROOT/landing"
ASSETS="$ROOT/assets"
PYTHON_BIN="${PYTHON_BIN:-python3}"
CUSTOM_DOMAIN="${CUSTOM_DOMAIN:-}"

if [[ -z "$CUSTOM_DOMAIN" && -f "$SITE/CNAME" ]]; then
  CUSTOM_DOMAIN="$(<"$SITE/CNAME")"
fi

if [[ -z "$CUSTOM_DOMAIN" ]] && git -C "$ROOT" cat-file -e HEAD:site/CNAME 2>/dev/null; then
  CUSTOM_DOMAIN="$(git -C "$ROOT" show HEAD:site/CNAME)"
fi

if [[ -x "$ROOT/.venv/bin/python3" ]]; then
  PYTHON_BIN="$ROOT/.venv/bin/python3"
fi

rm -rf "$SITE"
mkdir -p "$SITE"

"$PYTHON_BIN" -m sphinx -b html "$DOCS/hprlp" "$SITE/hprlp"
"$PYTHON_BIN" -m sphinx -b html "$DOCS/hprqp" "$SITE/hprqp"

cp -R "$LANDING"/. "$SITE"/
mkdir -p "$SITE/assets"
cp -R "$ASSETS"/. "$SITE/assets"/

touch "$SITE/.nojekyll"

if [[ -n "$CUSTOM_DOMAIN" ]]; then
  printf '%s' "$CUSTOM_DOMAIN" > "$SITE/CNAME"
fi

printf 'Done. Open "%s/index.html"\n' "$SITE"
