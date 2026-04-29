"""CLI entrypoint for audio-description.

Run with:
    python -m audio_description
    # or, after pip install:
    audio-description
"""

from __future__ import annotations

import sys

from audio_description import __version__

_HELP = f"""\
audio-description {__version__}

Usage:
  python -m audio_description [--help] [--version]

Commands (coming soon):
  describe    Generate audio descriptions for a video clip
  index       Index generated descriptions for retrieval

Options:
  -h, --help      Show this help message and exit
  --version       Print version and exit

Run 'python -m audio_description <command> --help' for command-specific options.
"""


def main(argv: list[str] | None = None) -> int:
    """Entry point for the audio-description CLI."""
    args = argv if argv is not None else sys.argv[1:]

    if not args or "-h" in args or "--help" in args:
        print(_HELP, end="")
        return 0

    if "--version" in args:
        print(f"audio-description {__version__}")
        return 0

    print(f"Unknown arguments: {args}", file=sys.stderr)
    print("Run 'python -m audio_description --help' for usage.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
