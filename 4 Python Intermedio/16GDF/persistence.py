import csv
from pathlib import Path
from datetime import datetime
from models import Category, Transaction

Date_FORMAT = "%d/%m/%Y"

class CSV_Storage:

    def __init__(self, categories_path="categories.csv", transactions_path="transactions.csv"):
        self.categories_path = Path(categories_path)
        self.transactions_path = Path(transactions_path)

    def load_categories(self):
        categories = {}

        if not self.categories_path.exists():
            return categories

        with self.categories_path.open("r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                categories[row["name"]] = Category(row["name"], row["color_hex"].upper())
        return categories

    def save_categories(self, categories):
        with self.categories_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "color_hex"])
            for cat in categories.values():
                writer.writerow([cat.name, cat.color_hex])

    def load_transactions(self, categories):
        transactions = []

        if not self.transactions_path.exists():
            return transactions

        with self.transactions_path.open("r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                date = datetime.strptime(row["date"], Date_FORMAT)
                description = row["title"]
                amount = float(row["amount"])
                category_name = row["category"]
                transaction_type = row["type"]
                category = categories.get(category_name, Category(category_name))
                transactions.append(Transaction(date, description, amount, category, transaction_type))
        return transactions

    def save_transactions(self, transactions):
        with self.transactions_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "title", "amount", "category", "type"])
            for transaction in transactions:
                writer.writerow([
                    transaction.date.strftime(Date_FORMAT),
                    transaction.title,
                    transaction.amount,
                    transaction.category.name,
                    transaction.type,
                ])
