import pytest
from logic import TransactionValidator, TransactionFilter
from models import Category, Transaction, Type_Income, Type_Expense
from datetime import datetime


def test_validate_amount_valid():
    assert TransactionValidator.validate_amount("10.5") == 10.5


def test_validate_amount_invalid():
    with pytest.raises(ValueError):
        TransactionValidator.validate_amount("abc")


def test_validate_date_invalid_format():
    with pytest.raises(ValueError):
        TransactionValidator.validate_date("2025-01-01")


def test_create_transaction_ok():
    cat = Category("Food")
    test = TransactionValidator.create_transaction("01/07/2025", "Pizza", "-40", cat, Type_Expense)
    assert test.title == "Pizza"
    assert test.amount == -40
    assert test.category == cat
    assert test.type == Type_Expense


def test_create_transaction_empty_title():
    cat = Category("Food")
    with pytest.raises(ValueError):
        TransactionValidator.create_transaction("01/07/2025", "   ", "10", cat, Type_Income)


def test_filter_by_date_range():
    cat = Category("Work")
    transaction1 = TransactionValidator.create_transaction("01/07/2025", "Salary", "1000", cat, Type_Income)
    transaction2 = TransactionValidator.create_transaction("10/07/2025", "Bonus", "200", cat, Type_Income)
    transaction3 = TransactionValidator.create_transaction("20/07/2025", "Extra", "300", cat, Type_Income)

    filtered = TransactionFilter.filter_by_date_range([transaction1, transaction2, transaction3], "01/07/2025", "15/07/2025")
    assert len(filtered) == 2


def test_compute_totals():
    cat = Category("Mixed")
    transaction1 = Transaction(datetime(2025, 7, 1), "Salary", 1000, cat, Type_Income)
    transaction2 = Transaction(datetime(2025, 7, 2), "Food", -100, cat, Type_Expense)

    totals = TransactionFilter.compute_totals([transaction1, transaction2])

    assert totals["income"] == 1000
    assert totals["expenses"] == 100
    assert totals["balance"] == 900


def test_filter_invalid_range():
    cat = Category("Work")
    transaction_test = TransactionValidator.create_transaction("01/07/2025", "Salary", "1000", cat, Type_Income)

    with pytest.raises(ValueError):
        TransactionFilter.filter_by_date_range([transaction_test], "10/07/2025", "01/07/2025")

