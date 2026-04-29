"""Tests for the audio_description CLI entrypoint."""

from audio_description import __version__
from audio_description.__main__ import main


def test_help_exits_zero():
    assert main(["--help"]) == 0


def test_help_no_args_exits_zero():
    assert main([]) == 0


def test_version_exits_zero():
    assert main(["--version"]) == 0


def test_unknown_arg_exits_nonzero():
    assert main(["unknown-command"]) != 0


def test_version_string():
    assert isinstance(__version__, str)
    assert len(__version__) > 0
