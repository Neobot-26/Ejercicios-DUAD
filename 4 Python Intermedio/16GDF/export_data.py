import csv

def export_movements_to_csv(data, output_file="Report_Movements.csv"):
    total_income = 0
    total_expenses = 0

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Headers
        writer.writerow(
            ["Date", "Title", "Amount", "Category", "Type"]
        )

        # Data_Info
        for row in data:
            writer.writerow(row)

            amount = float(row[2])

            if amount >= 0:
                total_income += amount
            else:
                total_expenses += abs(amount)

        # Empty Line
        writer.writerow([])
        writer.writerow(["Totals"])

        writer.writerow(
            ["Total Income", f"₡{total_income:.2f}"]
        )

        writer.writerow(
            ["Total Expenses", f"₡{total_expenses:.2f}"]
        )

        writer.writerow(
            ["Net Balance", f"₡{total_income-total_expenses:.2f}"]
        )

    return output_file