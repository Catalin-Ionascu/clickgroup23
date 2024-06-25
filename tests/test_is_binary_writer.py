import io
from click._compat import _is_binary_writer

def test_binarywriter():

    exception_stream = io.BytesIO()
    def raise_exception(*args, **kwargs):
        raise Exception("General exception")
    exception_stream.write = raise_exception
    assert _is_binary_writer(exception_stream, default=False) is False
    assert _is_binary_writer(exception_stream, default=True) is True


