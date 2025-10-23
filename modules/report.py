import os
import csv
from collections import defaultdict
from tabulate import tabulate
#import matplotlib.pyplot as plt

# -------------------------------
# Function: Load entries from CSV
# -------------------------------
def load_entries():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, "data", "expenses.csv")

    entries = []
    try:
        with open(csv_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    entries.append(row)
    except FileNotFoundError:
        print(f"CSV file not found at {csv_path}.")
    return entries

# -------------------------------
# Function: Monthly summary
# -------------------------------
def monthly_summary(entries):
    summary = defaultdict(lambda: {"income": 0, "expense": 0})

    for row in entries:
        try:
            date, type_, category, amount_str, description = row
            amount = float(amount_str.strip())
        except ValueError:
            print(f"Skipping row with invalid amount: {row}")
            continue

        month = date[:7]  # YYYY-MM
        summary[month][type_.lower()] += amount

    table = []
    for month, data in sorted(summary.items()):
        net = data["income"] - data["expense"]
        table.append([month, data["income"], data["expense"], net])

    print("\n--- Monthly Summary ---")
    print(tabulate(table, headers=["Month", "Total Income", "Total Expense", "Net Balance"], tablefmt="grid"))

# -------------------------------
# Function: Top expense categories
# -------------------------------
def top_expense_categories(entries, top_n=5):
    category_totals = defaultdict(float)

    for row in entries:
        try:
            type_, category, amount_str = row[1].lower(), row[2].lower(), row[3]
            amount = float(amount_str.strip())
        except ValueError:
            print(f"Skipping row with invalid amount: {row}")
            continue

        if type_ == "expense":
            category_totals[category] += amount

    sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)[:top_n]

    if not sorted_categories:
        print("No expense data available.")
        return

    print(f"\n--- Top {top_n} Expense Categories ---")
    print(tabulate(sorted_categories, headers=["Category", "Total Expense"], tablefmt="grid"))

    # Optional: Pie chart
    #labels = [cat for cat, amt in sorted_categories]
    #amounts = [amt for cat, amt in sorted_categories]
    #plt.figure(figsize=(6,6))
    #plt.pie(amounts, labels=labels, autopct="%1.1f%%", startangle=140)
    #plt.title(f"Top {top_n} Expense Categories")
    #plt.show()

# -------------------------------
# Function: Overall summary
# -------------------------------
def overall_summary(entries):
    total_income = 0
    total_expense = 0

    for row in entries:
        try:
            type_, amount_str = row[1].lower(), row[3]
            amount = float(amount_str.strip())
        except ValueError:
            print(f"Skipping row with invalid amount: {row}")
            continue

        if type_ == "income":
            total_income += amount
        elif type_ == "expense":
            total_expense += amount

    net_balance = total_income - total_expense

    table = [
        ["Total Income", total_income],
        ["Total Expense", total_expense],
        ["Net Balance", net_balance]
    ]
    print("\n--- Overall Summary ---")
    print(tabulate(table, headers=["Type", "Amount"], tablefmt="grid"))

# -------------------------------
# Function: Report Menu
# -------------------------------
def report_menu():
    entries = load_entries()
    if not entries:
        print("No data to generate reports.")
        return

    while True:
        print("\n--- REPORT MENU ---")
        print("1. Monthly Summary")
        print("2. Top Expense Categories")
        print("3. Overall Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            monthly_summary(entries)
        elif choice == "2":
            top_expense_categories(entries)
        elif choice == "3":
            overall_summary(entries)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# -------------------------------
# Run menu if executed directly
# -------------------------------
if __name__ == "__main__":
    report_menu()
