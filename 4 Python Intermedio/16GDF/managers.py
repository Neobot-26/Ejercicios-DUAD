from models import Category
from logic import TransactionValidator, TransactionFilter


class CategoryManager:
    def __init__(self, storage):
        self.storage = storage
        self.categories = storage.load_categories()

    def add_category(self, name, color):
        self.categories[name] = Category(name, color.upper())
        self.storage.save_categories(self.categories)

    def get_all(self):
        return self.categories


class TransactionManager:
    def __init__(self, storage, category_manager):
        self.storage = storage
        self.category_manager = category_manager
        self.transactions = storage.load_transactions(category_manager.categories)

    def add_transaction(self, date, title, amount, category_name, transaction_type):
        category = self.category_manager.categories[category_name]
        new_transaction = TransactionValidator.create_transaction(date, title, amount, category, transaction_type)
        self.transactions.append(new_transaction)
        self.storage.save_transactions(self.transactions)

    def filter(self, start, end):
        return TransactionFilter.filter_by_date_range(self.transactions, start, end)

    def totals(self):
        return TransactionFilter.compute_totals(self.transactions)
