import pytest

from click.core import __getattr__
from click.core import _BaseCommand
from click.core import _MultiCommand


def test_getattr_base_command():
    with pytest.warns(
        DeprecationWarning,
        match="'BaseCommand' is deprecated and will be removed in Click 9.0. Use"
        "'Command' instead.",
    ):
        assert __getattr__("BaseCommand") == _BaseCommand


def test_getattr_multi_command():
    with pytest.warns(
        DeprecationWarning,
        match="'MultiCommand' is deprecated and will be removed in Click 9.0. Use"
        "'Group' instead.",
    ):
        assert __getattr__("MultiCommand") == _MultiCommand
