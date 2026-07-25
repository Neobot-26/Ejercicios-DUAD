from datetime import datetime

Type_Income = "Income"
Type_Expense = "Expense"


class Category:
    def __init__(self, name, color_hex="#FFFFFF"):
        self.name = name
        self.color_hex = color_hex


class Transaction:
    def __init__(self, date, title, amount, category, ttype):
        self.date = date
        self.title = title
        self.amount = amount
        self.category = category
        self.type = ttype

    def is_income(self):
        return self.type == Type_Income

    def is_expense(self):
        return self.type == Type_Expense
