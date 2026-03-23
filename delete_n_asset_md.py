#!/usr/bin/env python3
"""Удаляет файлы вида <N>_asset.md (N — только цифры) под заданным корнем."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERN = re.compile(r"^\d+_asset\.md$")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        type=Path,
        help="Корень обхода (по умолчанию текущая директория)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Только показать пути, не удалять",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    if not root.is_dir():
        print(f"Не каталог: {root}", file=sys.stderr)
        return 1

    matches = sorted(p for p in root.rglob("*") if p.is_file() and PATTERN.match(p.name))
    if not matches:
        print("Файлов не найдено.")
        return 0

    for path in matches:
        if args.dry_run:
            print(f"would delete: {path}")
        else:
            path.unlink()
            print(f"deleted: {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
