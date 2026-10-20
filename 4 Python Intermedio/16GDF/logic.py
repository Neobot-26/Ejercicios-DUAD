from datetime import datetime, date
from models import Transaction, Type_Income, Type_Expense
from persistence import Date_FORMAT


class TransactionValidator:

    @staticmethod
    def validate_amount(text):
        try:
            return float(text)
        except ValueError:
            raise ValueError("Invalid amount")

    @staticmethod
    def validate_date(text):
        try:
            dt = datetime.strptime(text, Date_FORMAT)
        except ValueError:
            raise ValueError("Invalid date format (use dd/mm/yyyy)")

        if dt.date() > date.today():
            raise ValueError("Date cannot be in the future")

        return dt

    @staticmethod
    def create_transaction(date_str, title, amount_str, category, ttype):
        if not title.strip():
            raise ValueError("Description cannot be empty")

        amount = TransactionValidator.validate_amount(amount_str)
        dt = TransactionValidator.validate_date(date_str)

        if ttype not in (Type_Income, Type_Expense):
            raise ValueError("Invalid transaction type")

        return Transaction(dt, title.strip(), amount, category, ttype)


class TransactionFilter:

    @staticmethod
    def filter_by_date_range(transactions, start_str, end_str):
        start = TransactionValidator.validate_date(start_str)
        end = TransactionValidator.validate_date(end_str)

        if start > end:
            raise ValueError("Start date cannot be greater than end date")

        return [t for t in transactions if start <= t.date <= end]

    @staticmethod
    def compute_totals(transactions):
        income = sum(transaction.amount for transaction in transactions if transaction.is_income())
        expenses = sum(abs(transaction.amount) for transaction in transactions if transaction.is_expense())

        return {
            "income": income,
            "expenses": expenses,
            "balance": income - expenses,
        }
