import io
from click._compat import _is_binary_reader

def test_exception_binaryreader():

    exception_stream = io.BytesIO(b"test")
    def raise_exception(*args, **kwargs):
        raise Exception("stream error")
    exception_stream.read = raise_exception
    assert _is_binary_reader(exception_stream) is False
