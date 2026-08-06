from Ejercicio_3 import sum_values


def test_sum_positive_numbers():
    data = [1, 2, 3, 4, 5]

    result = sum_values(data)

    assert result == 15


def test_sum_negative_numbers():
    data = [-1, -2, -3, -4]

    result = sum_values(data)

    assert result == -10


def test_sum_mixed_numbers():
    data = [10, -5, 8, -3]

    result = sum_values(data)

    assert result == 10