#!/usr/bin/env bash
# Удаляет все файлы вида <N>_conststrains.md под корнем репозитория.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ "${1:-}" == "--dry-run" ]]; then
  find . -type f -name '*_conststrains.md' -print
  exit 0
fi

find . -type f -name '*_conststrains.md' -print -delete
