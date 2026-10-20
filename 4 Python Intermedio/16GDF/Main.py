import FreeSimpleGUI as sg
import csv
from persistence import CSV_Storage, Date_FORMAT
from managers import CategoryManager, TransactionManager
from interfaces import create_main_window, category_window, transaction_window
from models import Type_Income, Type_Expense


class FinanceApp:

    def __init__(self):
        self.storage = CSV_Storage()
        self.category_manager = CategoryManager(self.storage)
        self.transaction_manager = TransactionManager(self.storage, self.category_manager)

        self.window = create_main_window(
            self.transaction_manager.transactions,
            self.category_manager.categories
        )
        self.update_table(self.transaction_manager.transactions)

    def update_table(self, transactions):
        data = [
            [transac.date.strftime("%d/%m/%Y"), transac.title, transac.amount, transac.category.name, transac.type]
            for transac in transactions
        ]
        row_colors = [(i, transac.category.color_hex) for i, transac in enumerate(transactions)]
        self.window["-TABLE-"].update(values=data, row_colors=row_colors)

    def export_csv(self, transactions, path="export.csv"):
        totals = self.transaction_manager.totals()

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Title", "Amount", "Category", "Type"])

            for transaction in transactions:
                writer.writerow([
                    transaction.date.strftime(Date_FORMAT),
                    transaction.title,
                    transaction.amount,
                    transaction.category.name,
                    transaction.type,
                ])

            writer.writerow([])
            writer.writerow(["Totals"])
            writer.writerow([f"Income: {totals['income']}"])
            writer.writerow([f"Expenses: {totals['expenses']}"])
            writer.writerow([f"Balance: {totals['balance']}"])

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            self.window["-MSG-"].update("")

            if event == "-BTN_CAT-":
                category_window(self.category_manager)
                self.update_table(self.transaction_manager.transactions)

            elif event == "-BTN_EXPENSE-":
                transaction_window(self.transaction_manager, Type_Expense)
                self.update_table(self.transaction_manager.transactions)

            elif event == "-BTN_INCOME-":
                transaction_window(self.transaction_manager, Type_Income)
                self.update_table(self.transaction_manager.transactions)

            elif event == "-BTN_FILTER-":
                try:
                    filtered = self.transaction_manager.filter(
                        values["-DATE_START-"],
                        values["-DATE_END-"]
                    )
                    self.update_table(filtered)
                    self.window["-MSG-"].update(
                        f"Filtering from {values['-DATE_START-']} to {values['-DATE_END-']}"
                    )
                except Exception as e:
                    self.window["-MSG-"].update(str(e))

            elif event == "-BTN_CSV-":
                self.export_csv(self.transaction_manager.transactions)
                self.window["-MSG-"].update("CSV exported successfully.")

        self.window.close()


if __name__ == "__main__":
    FinanceApp().run()

