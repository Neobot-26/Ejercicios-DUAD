import pytest
from Divide import divide


def test_divide_success():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="You can't divide by zero"):
        divide(10, 0)


def test_divide_with_string():
    with pytest.raises(TypeError):
        divide("10", 2)