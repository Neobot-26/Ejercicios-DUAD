from datetime import datetime
def filter_by_dates(data, start_date, end_date):
    start = datetime.strptime(start_date, "%d/%m/%Y")
    end = datetime.strptime(end_date, "%d/%m/%Y")
    if start < end:
        filtered = []
        for row in data:
            movement_date = datetime.strptime(row[0], "%d/%m/%Y")
            if start <= movement_date <= end:
                filtered.append(row)
        return filtered

def validate_filter_dates(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%d/%m/%Y")
        end = datetime.strptime(end_date, "%d/%m/%Y")

        if start > end:
            return False, "The start date must be earlier than or equal to the end date."
        return True, ""
    except ValueError:
        return False, "Invalid date. Please use dd/mm/yyyy."

def validate_date(verify_date):
    try:
        actual_date = datetime.now()
        entered_date = datetime.strptime(verify_date,"%d/%m/%Y")
        if entered_date > actual_date:
            return False, "Date entered must be earlier than or equal to today."
        return True, ""
    except ValueError:
        return False, "Invalid date. Please use dd/mm/yyyy."