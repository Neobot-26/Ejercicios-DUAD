from Ejercicio_5 import new_string


def test_only_lowercase():
    result = new_string("python")

    assert result == (6, 0)


def test_only_uppercase():
    result = new_string("PYTHON")

    assert result == (0, 6)


def test_mixed_characters():
    result = new_string("PyThOn123!")

    assert result == (3, 3)