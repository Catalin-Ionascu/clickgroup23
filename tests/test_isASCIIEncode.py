import pytest

from click._compat import is_ascii_encoding 

def test_is_ascii_encoding_invalid_encoding():
    assert is_ascii_encoding('invalid-encoding') == False