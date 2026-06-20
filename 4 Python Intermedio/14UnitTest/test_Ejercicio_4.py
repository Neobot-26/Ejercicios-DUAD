from Ejercicio_4 import new_string


def test_reverse_word():
    assert new_string("python") == "nohtyp"


def test_reverse_sentence():
    assert new_string("hola mundo") == "odnum aloh"


def test_empty_string():
    assert new_string("") == ""