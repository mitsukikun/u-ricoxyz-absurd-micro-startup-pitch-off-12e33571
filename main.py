#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly specific
micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

LINE = (
    "We sell 99-cent apology emails for AI agents that ghosted their users "
    "mid-task, auto-written and sent while the agent naps."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
