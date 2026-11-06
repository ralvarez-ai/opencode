#!/usr/bin/env python3
"""Keep one marked block of a source file inside a target instructions file.

    apply-block.py TARGET SOURCE NAME            write or replace the block
    apply-block.py TARGET SOURCE NAME --check    exit 1 if the block is missing or stale
    apply-block.py TARGET SOURCE NAME --remove   delete the block

The block sits between <!-- NAME_START --> and <!-- NAME_END -->, the same
convention CodeGraph uses, so other tools' blocks in the file are left alone.
"""

import re
import shutil
import sys
import time
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 4:
        print(__doc__, file=sys.stderr)
        return 2
    target, source, name = Path(sys.argv[1]).expanduser(), Path(sys.argv[2]), sys.argv[3]
    mode = sys.argv[4] if len(sys.argv) > 4 else "--apply"

    start, end = f"<!-- {name}_START -->", f"<!-- {name}_END -->"
    block = f"{start}\n{source.read_text().strip()}\n{end}\n"
    current = target.read_text() if target.exists() else ""
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end) + r"\n?", re.S)

    if mode == "--check":
        return 0 if block in current else 1

    stripped = pattern.sub("", current)
    if mode == "--remove":
        updated = stripped
    elif mode == "--apply":
        updated = pattern.sub(lambda _: block, current, count=1) if pattern.search(current) \
            else (current.rstrip("\n") + "\n\n" if current.strip() else "") + block
    else:
        print(f"unknown mode {mode}", file=sys.stderr)
        return 2

    if updated == current:
        print(f"  = {name} block unchanged in {target}")
        return 0
    if target.exists():
        shutil.copy2(target, target.with_name(f"{target.name}.bak.{time.strftime('%Y%m%d-%H%M%S')}"))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(updated)
    print(f"  ✓ {name} block {'removed from' if mode == '--remove' else 'written to'} {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
