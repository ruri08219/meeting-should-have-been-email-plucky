"""Write the one-line meeting joke to /output/entry.txt.

Standard library only. The entry is a single line of plain text, at most
200 characters, about a meeting that should have been an email.
"""

import os
import sys

ENTRY = (
    "The host read aloud the email we'd all already read, "
    "then asked if anyone had questions about the email."
)


def main() -> int:
    text = ENTRY
    if not text or not text.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(text) > 200:
        print("error: entry is %d chars, over the 200 limit" % len(text),
              file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %s (%d chars)" % (out_path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
