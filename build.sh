#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HPR_PYTHON="${PYTHON_BIN:-python3}"
if [[ -x "$ROOT/.venv/bin/python3" ]]; then
  HPR_PYTHON="$ROOT/.venv/bin/python3"
fi
exec "$HPR_PYTHON" "$ROOT/tools/build_site.py" "$@"
