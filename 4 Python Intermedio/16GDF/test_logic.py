from unittest.mock import mock_open, patch

from logic import (
    CategoryManager,
    MovementManager,
    data_empty,
    verify_data,
    list_categories
)


# ==========================
# Tests for data_empty
# ==========================

def test_data_empty_with_empty_string():
    assert data_empty("") == 0


def test_data_empty_with_text():
    assert data_empty("Food") == 1


# ==========================
# Tests for list_categories
# ==========================

def test_list_categories():
    data1 = ["Food", "Transport"]
    data2 = ["red", "blue"]

    expected = [
        ["Food", "red"],
        ["Transport", "blue"]
    ]

    assert list_categories(data1, data2) == expected


# ==========================
# Tests for CategoryManager
# ==========================

def test_read_categories():
    csv_content = (
        "Category,Color\n"
        "Food,red\n"
        "Transport,blue\n"
    )

    manager = CategoryManager("categories.csv")

    with patch("builtins.open", mock_open(read_data=csv_content)):
        categories, colors = manager.read_categories()

    assert categories == ["Food", "Transport"]
    assert colors == ["red", "blue"]


def test_get_categories():
    manager = CategoryManager()

    with patch.object(
        manager,
        "read_categories",
        return_value=(["Food"], ["red"])
    ):
        categories, colors = manager.get_categories()

    assert categories == ["Food"]
    assert colors == ["red"]


def test_write_category():
    manager = CategoryManager()

    m = mock_open()

    with patch("builtins.open", m):
        manager.write_category(["Food", "red"])

    m.assert_called_once()


# ==========================
# Tests for MovementManager
# ==========================

def test_read_movements():
    csv_content = (
        "Date,Description,Amount\n"
        "01/01/2026,Salary,1000\n"
        "02/01/2026,Food,-10\n"
    )

    manager = MovementManager("Gestor.csv")

    with patch("builtins.open", mock_open(read_data=csv_content)):
        data = manager.read_movements()

    assert len(data) == 2
    assert data[0] == ["01/01/2026", "Salary", "1000"]
    assert data[1] == ["02/01/2026", "Food", "-10"]


def test_write_movements():
    manager = MovementManager()

    m = mock_open()

    with patch("builtins.open", m):
        manager.write_movements(
            ["01/01/2026", "Salary", "1000"]
        )

    m.assert_called_once()


# ==========================
# Tests for verify_data
# ==========================

def test_verify_data_valid_category():

    with patch.object(
        CategoryManager,
        "get_categories",
        return_value=(["food", "transport"], ["red", "blue"])
    ):
        assert verify_data("food") == 1


def test_verify_data_invalid_category():

    with patch.object(
        CategoryManager,
        "get_categories",
        return_value=(["Food", "Transport"], ["red", "blue"])
    ):
        assert verify_data("Health") == 0


def test_verify_data_empty_string():

    with patch.object(
        CategoryManager,
        "get_categories",
        return_value=(["Food", "Transport"], ["red", "blue"])
    ):
        assert verify_data("") == 0