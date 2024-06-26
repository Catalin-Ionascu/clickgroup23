import pytest
from click._compat import should_strip_ansi


def test_no_color_no_stream():
    assert should_strip_ansi(None, None) == True

def test_color():
    assert should_strip_ansi(None, True) == False
