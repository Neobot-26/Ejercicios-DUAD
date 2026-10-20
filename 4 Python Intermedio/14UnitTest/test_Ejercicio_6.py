from Ejercicio_6 import string_to_list, sort_list, list_to_string


def test_sort_three_words():
    sentence = "pera-manzana-banano"

    result = list_to_string(
        sort_list(
            string_to_list(sentence)
        )
    )

    assert result == "banano-manzana-pera"


def test_sort_already_sorted():
    sentence = "a-b-c-d"

    result = list_to_string(
        sort_list(
            string_to_list(sentence)
        )
    )

    assert result == "a-b-c-d"


def test_sort_five_words():
    sentence = "zorro-casa-avion-barco-dado"

    result = list_to_string(
        sort_list(
            string_to_list(sentence)
        )
    )

    assert result == "avion-barco-casa-dado-zorro"