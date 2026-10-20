from Ejercicio_7 import verification


def test_mixed_numbers():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = verification(data)

    assert result == [2, 3, 5, 7]


def test_all_prime_numbers():
    data = [2, 3, 5, 7, 11, 13]

    result = verification(data)

    assert result == [2, 3, 5, 7, 11, 13]


def test_no_prime_numbers():
    data = [1, 4, 6, 8, 9, 10, 12]

    result = verification(data)

    assert result == []