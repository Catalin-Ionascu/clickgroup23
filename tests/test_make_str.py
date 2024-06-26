from click.utils import make_str

def test_value_of_type_bytes():
    assert make_str(b'hello') == "hello"
def test_invalid_value():
    assert make_str(b'\xff') == "�"