import pytest
from click.utils import get_text_stream 

def test_get_text_stream_valid():
    stream = get_text_stream('stdout')
    assert stream is not None

def test_get_text_stream_invalid():
    with pytest.raises(TypeError) as excinfo:
        get_text_stream('invalid_stream_name')  # type: ignore
    assert "Unknown standard stream" in str(excinfo.value)