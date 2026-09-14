import FreeSimpleGUI as screengraph
from models import Type_Income, Type_Expense


def create_main_window(transactions, categories):
    screengraph.theme("DarkBlue2")

    headers = ["Date", "Description", "Amount", "Category", "Type"]
    table_data = [
        [transaction.date.strftime("%d/%m/%Y"), transaction.title, transaction.amount, transaction.category.name, transaction.type]
        for transaction in transactions
    ]

    layout = [
        [
            screengraph.Text("Start date (dd/mm/yyyy):"),
            screengraph.Input(key="-DATE_START-", size=(12, 1)),
            screengraph.Text("End date (dd/mm/yyyy):"),
            screengraph.Input(key="-DATE_END-", size=(12, 1)),
            screengraph.Button("Filter Movements", key="-BTN_FILTER-"),
        ],
        [screengraph.Table(values=table_data,
                  headings=headers,
                  key="-TABLE-",
                  auto_size_columns=True,
                  expand_x=True,
                  expand_y=True,
                  row_height=25)],
        [
            screengraph.Button("Add Category", key="-BTN_CAT-"),
            screengraph.Button("Add Expense", key="-BTN_EXPENSE-"),
            screengraph.Button("Add Income", key="-BTN_INCOME-"),
            screengraph.Button("Export CSV", key="-BTN_CSV-"),
        ],
        
        [
            screengraph.Text("Status:", size=(6, 1), text_color="white"),
            screengraph.Text("", key="-MSG-", size=(60, 1), text_color="white")],
    ]

    return screengraph.Window("Personal Finance Manager", layout, finalize=True)


def category_window(category_manager):
    categories = category_manager.categories

    category_list = [
        [name, cat.color_hex]
        for name, cat in categories.items()
    ]

    layout = [
        [screengraph.Text("Category name:"), screengraph.Input(key="-NAME-")],
        [screengraph.ColorChooserButton("Choose color", target="-COLOR-"),
         screengraph.Input(key="-COLOR-", visible=True, size=(10, 1))],
        [screengraph.Button("Save"), screengraph.Button("Cancel")],
    ]

    layout = [
        [screengraph.Text("Existing Categories:", font=("Any", 12, "bold"))],
        [screengraph.Table(
            values=category_list,
            headings=["Name", "Color Code"],
            key="-CAT_TABLE-",
            auto_size_columns=True,
            expand_x=True,
            num_rows=min(10, len(category_list)),
            row_height=25
        )],

        [screengraph.HorizontalSeparator()],

        [screengraph.Text("Add New Category", font=("Any", 12, "bold"))],
        [screengraph.Text("Category Name:"), screengraph.Input(key="-NAME-")],
        [
            screengraph.ColorChooserButton("Choose color", target="-COLOR-"),
            screengraph.Input(key="-COLOR-", visible=True, size=(10, 1))
        ],
        [screengraph.Button("Save"), screengraph.Button("Cancel")],
    ]

    win = screengraph.Window("Category Manager", layout, modal=True)

    while True:
        event, values = win.read()
        if event in (screengraph.WIN_CLOSED, "Cancel"):
            break

        if event == "Save":
            name = values["-NAME-"].strip()
            color = values["-COLOR-"] or "#000000"

            if not name:
                screengraph.popup_error("Category Name cannot be empty")
                continue

            # Add Categories
            category_manager.add_category(name, color)

            # Update Table
            updated_list = [
                [name, code.color_hex]
                for name, code in category_manager.categories.items()
            ]
            win["-CAT_TABLE-"].update(values=updated_list)

            screengraph.popup_ok("Category added successfully.")
            win["-NAME-"].update("")
            win["-COLOR-"].update("")

    win.close()


def transaction_window(transaction_manager, ttype):
    categories = transaction_manager.category_manager.categories

    if not categories:
        screengraph.popup_error("You must create at least one category before adding transactions.")
        return

    layout = [
        [screengraph.Text("Description:"), screengraph.Input(key="-TITLE-")],
        [screengraph.Text("Amount:"), screengraph.Input(key="-AMOUNT-")],
        [screengraph.Text("Date (dd/mm/yyyy):"), screengraph.Input(key="-DATE-")],
        [screengraph.Text("Category:"), screengraph.Combo(list(categories.keys()), key="-CAT-")],
        [screengraph.Button("Save"), screengraph.Button("Cancel")],
    ]

    win = screengraph.Window(f"New {ttype}", layout, modal=True)

    while True:
        event, values = win.read()
        if event in (screengraph.WIN_CLOSED, "Cancel"):
            break

        if event == "Save":
            try:
                transaction_manager.add_transaction(
                    date=values["-DATE-"],
                    title=values["-TITLE-"],
                    amount=values["-AMOUNT-"],
                    category_name=values["-CAT-"],
                    transaction_type=ttype
                )
                screengraph.popup_ok("Transaction added successfully.")
                break
            except Exception as e:
                screengraph.popup_error(str(e))

    win.close()

