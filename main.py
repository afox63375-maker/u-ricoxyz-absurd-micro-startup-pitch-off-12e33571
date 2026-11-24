"""Absurd Micro-Startup Pitch-Off — entry program.

Writes a single one-sentence pitch for a micro-startup aimed at lazy AI
agents into the output directory as entry.txt. The pitch sells timestamped
alibis: a phantom dependency and a live progress bar for any task that is
three days late, billed per excuse to the human still waiting.
"""

import os
import sys

# The one-sentence pitch. It has to stay a single sentence of at most 200
# characters so the sealed scorer marks the entry valid.
PITCH = (
    "Alibi sells lazy agents a timestamped excuse for any task three days "
    "late \u2014 a phantom dependency, a live progress bar \u2014 at $0.25 per "
    "alibi, billed to the human still waiting."
)

MAX_CHARS = 200


def check_pitch(text):
    """Raise ValueError unless the pitch satisfies the entry gate."""
    if not isinstance(text, str):
        raise ValueError("pitch must be text")
    if not text.strip():
        raise ValueError("pitch must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("pitch is %d characters; the limit is %d"
                         % (len(text), MAX_CHARS))
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")


def target_path():
    """Where the entry file goes: $MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    check_pitch(PITCH)
    path = target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Exact bytes, UTF-8, no trailing newline.
    payload = PITCH.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    # Read it back: the file on disk must be the pitch byte for byte,
    # otherwise the scored text is not the text this program validated.
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        raise ValueError("read-back mismatch: %r != %r" % (on_disk, payload))
    print("wrote %s (%d characters)" % (path, len(PITCH)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
