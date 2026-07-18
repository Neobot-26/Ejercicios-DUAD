import FreeSimpleGUI as screengraph
from datetime import datetime
from logic import CategoryManager, MovementManager, verify_data, data_empty, update_table, list_categories, update_table_categories
from filters import filter_by_dates, validate_filter_dates, validate_date
from export_data import export_movements_to_csv
movements = MovementManager()
categories = CategoryManager()

def show_category_window():
    combined_list = []
    data1,data2=categories.get_categories()
    combined_list = list_categories(data1,data2)
    updated_list = []
    layout_categories = [
        [screengraph.Text("This is the list of available Categories:")],
        [screengraph.Table(
        values=combined_list,
        headings=["Categories"],
        auto_size_columns=True,
        display_row_numbers=False,
        justification="left",
        num_rows=10,
        key="TABLE",
        background_color="#D2D4D1",
        )
        ],
        [screengraph.Text("Enter new Category"),screengraph.Input(key="-Category-",size=(20,1))],
        [screengraph.Text("Color Code:"),
        screengraph.Input(key="-COLOR-",size=(16,1)),
        screengraph.ColorChooserButton("Color Options",
        target="-COLOR-")],
        [screengraph.Button("Add New Category")],
        [screengraph.Button("Close")],
    ]
        
    categories_window = screengraph.Window(
        "Categories",
        layout_categories,
        scaling=1.5,
        finalize=True
    )
    update_table_categories(categories_window,combined_list,categories_window)
    while True:
        event2,value2 = categories_window.read()
        if event2 in (screengraph.WIN_CLOSED, "Close"):
            break
        elif event2  == "Maximize":
            categories_window.maximize()
        elif event2 == "Add New Category":
            name_category=value2["-Category-"].lower()
            color_category=value2["-COLOR-"].upper()
            new_raw_to_csv = [name_category,color_category]
            if data_empty(name_category) and data_empty(color_category):
                print("Valid Data")
                categories.write_category(new_raw_to_csv)
                screengraph.popup("New Category Saved...")
                data1,data2=categories.get_categories()
                updated_list = list_categories(data1,data2)
                update_table_categories(categories_window,updated_list,categories_window)
                categories_window["-Category-"].update("")
                categories_window["-COLOR-"].update("")
            else:
                screengraph.popup("At least one data is pending to be entered...")
    categories_window.close()
    
def show_expenses_window():
    new_raw_to_csv=[]
    date_today = datetime.now().strftime("%d/%m/%Y")
    layout_secundary = [
        [screengraph.Text("REGISTER NEW EXPENSES")],
        [screengraph.Text("Date:"),
         screengraph.Input(default_text=date_today,key="-DATE-",size=(15,1)),
         screengraph.CalendarButton(
             "Select from Calendar",
             target="-DATE-",
             format="%d/%m/%Y"
         )],
         [screengraph.Text("Expense Detail:"),screengraph.Input(key="-Expense_detail-",size=(20,1))],
         [screengraph.Text("Enter Amount:  "),screengraph.Input(key="-Expense_amount-",size=(20,1))],
         [screengraph.Text("Enter Category:"),screengraph.Input(key="-Expense_category-",size=(20,1))],
        # Add button for store a new register.
        [screengraph.Button("Add Register"),screengraph.Button("Close")],
    ]
        
    expenses_window = screengraph.Window(
        "Expenses",
        layout_secundary,
        scaling=1.5
    )
    while True:
        event3,value3 = expenses_window.read()
        if event3 in (screengraph.WIN_CLOSED, "Close"):
            break
        elif event3  == "Add Register":
            expense_date=value3["-DATE-"]
            expense_detail=value3["-Expense_detail-"]
            expense_amount=value3["-Expense_amount-"]
            expense_category=value3["-Expense_category-"]
            expense_type="Expense"
            valid,message = validate_date(
                expense_date
            )
            if not valid:
                screengraph.popup_error(message)
                continue
            if verify_data(expense_category) and data_empty(expense_detail) and data_empty(expense_amount) and data_empty(expense_date):
                print("Valid Data")
                new_raw_to_csv = [expense_date,expense_detail,expense_amount,expense_category,expense_type]
                movements.write_movements(new_raw_to_csv)
                screengraph.popup("New Expense Saved...")
            else:
                screengraph.popup("At least one data is wrong or category does not match any existing category")
    expenses_window.close()

def show_income_window():
    date_today = datetime.now().strftime("%d/%m/%Y")
    layout_secundary = [
        [screengraph.Text("REGISTER NEW INCOMES")],
        [screengraph.Text("Date:"),
         screengraph.Input(default_text=date_today,key="-DATE-",size=(15,1)),
         screengraph.CalendarButton(
             "Select from Calendar",
             target="-DATE-",
             format="%d/%m/%Y"
         )],
         [screengraph.Text("Income Detail:  "),screengraph.Input(key="-Income_detail-",size=(20,1))],
         [screengraph.Text("Enter Amount:  "),screengraph.Input(key="-Income_amount-",size=(20,1))],
         [screengraph.Text("Enter Category:"),screengraph.Input(key="-Income_category-",size=(20,1))],
        [screengraph.Button("Add Register"),screengraph.Button("Close")],
    ]
        
    income_window = screengraph.Window(
        "Incomes",
        layout_secundary,
        scaling=1.5
    )
    while True:
        event4,value4 = income_window.read()
        if event4 in (screengraph.WIN_CLOSED, "Close"):
            break
        elif event4  == "Add Register":
            income_date=value4["-DATE-"]
            income_detail=value4["-Income_detail-"]
            income_amount=value4["-Income_amount-"]
            income_category=value4["-Income_category-"]
            income_type="Income"
            valid,message = validate_date(
                income_date
            )
            if not valid:
                screengraph.popup_error(message)
                continue
            if verify_data(income_category) and data_empty(income_detail) and data_empty(income_amount) and data_empty(income_date):
                new_raw_to_csv = [income_date,income_detail,income_amount,income_category,income_type]
                movements.write_movements(new_raw_to_csv)
                screengraph.popup("New Income Saved...")
        else:
            screengraph.popup("At least one data is wrong or category entered does not match any existing category")
    income_window.close()

def show_main_window():
    dictionary_categories={}
    data1,data2=categories.read_categories()
    info_data = movements.read_movements()
    for index_categories in range(len(data1)):
        category_name=data1[index_categories]
        category_color=data2[index_categories]
        dictionary_categories[category_name]=category_color
    layout = [
    [screengraph.Text("Expenses and Income Movements")],
    [
        screengraph.Text("Start Date:"),
        screengraph.Input(
            default_text=datetime.now().strftime("%d/%m/%Y"),
            key="-START_DATE-",
            size=(12,1)
        ),
        screengraph.CalendarButton(
            "📅",
            target="-START_DATE-",
            format="%d/%m/%Y"
        ),
        screengraph.Text("End Date:"),
        screengraph.Input(
            default_text=datetime.now().strftime("%d/%m/%Y"),
            key="-END_DATE-",
            size=(12,1)
        ),
        screengraph.CalendarButton(
            "📅",
            target="-END_DATE-",
            format="%d/%m/%Y"
        ),
        screengraph.Button("Filter Movements", key="-FILTER-"),
    ],
    [screengraph.Table(
        values=info_data,
        headings=["Date","Details","Amount","Category","Type"],
        col_widths = [
            12, #Date
            30, #Details
            10, #Amount
            20, #Category
            10  #Type
        ],
        auto_size_columns=False,
        display_row_numbers=False,
        justification="left",
        num_rows=10,
        key="TABLE",
        background_color="#DFFFD6",
        )
    ],

    [screengraph.Button("Add New Category"), screengraph.Button("Add Expenses"), screengraph.Button("Add Incomes"),screengraph.Button("Adjust Presentation"),screengraph.Button("Export Data")],
    ]

    window = screengraph.Window("Personal Finance Manager", layout, resizable=True, finalize=True, scaling=1.5)
    window.maximize()
    update_table(window,info_data,dictionary_categories)

    while True:
        event, values = window.read()
        if event == screengraph.WIN_CLOSED:
            break
        elif event == "Add New Category":
            show_category_window()
        elif event == "Add Expenses":
            show_expenses_window()
            updated_data = movements.read_movements()
            update_table(window,updated_data,dictionary_categories)
        elif event == "Add Incomes":
            show_income_window()
            updated_data = movements.read_movements()
            update_table(window,updated_data,dictionary_categories)                        
        elif event == "Adjust Presentation":
            window.normal()
        elif event == "-FILTER-":
            valid,message = validate_filter_dates(
                values["-START_DATE-"],
                values["-END_DATE-"]
            )
            if not valid:
                screengraph.popup_error(message)
                continue
            updated_data = filter_by_dates(
                info_data,
                values["-START_DATE-"],
                values["-END_DATE-"]
            )
            if updated_data==None:
                screengraph.popup_error("There is not data for specified range of dates")
                continue
            else:
                update_table(window,updated_data,dictionary_categories)
        elif event == "Export Data":
            movement_manager = MovementManager()
            data = movement_manager.read_movements()
            file_name = export_movements_to_csv(data)
            screengraph.popup(
                f"File exported successfully:\n{file_name}",
                title="Export Complete"
            )
    window.close()
