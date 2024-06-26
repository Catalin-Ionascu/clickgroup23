from click._winconsole import _WindowsConsoleWriter
from click._winconsole import ERROR_NOT_ENOUGH_MEMORY
from click._winconsole import ERROR_SUCCESS


def test_get_error_message_success():
    test = _WindowsConsoleWriter(handle="test_handle")
    assert test._get_error_message(ERROR_SUCCESS) == "ERROR_SUCCESS"


def test_get_error_message_not_enough_memory():
    test = _WindowsConsoleWriter(handle="test_handle")
    assert test._get_error_message(ERROR_NOT_ENOUGH_MEMORY) == "ERROR_NOT_ENOUGH_MEMORY"


def test_get_error_message_other():
    test = _WindowsConsoleWriter(handle="test_handle")
    errno = 999
    assert test._get_error_message(errno) == f"Windows error {errno}"
