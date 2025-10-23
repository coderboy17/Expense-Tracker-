import os
import csv
from tabulate import tabulate

# -------------------------------
# Function: Load all entries from CSV
# -------------------------------
def load_entries():
    """
    Reads all rows from data/expenses.csv and returns a list of entries.
    Each entry is a list: [date, type, category, amount, description]
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))  # go up from modules/
    csv_path = os.path.join(base_dir, "data", "expenses.csv")

    entries = []  # to store all rows
    try:
        with open(csv_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:  # skip empty rows
                    entries.append(row)
    except FileNotFoundError:
        print(f"CSV file not found at {csv_path}. Please check the path.")

    return entries


# -------------------------------
# Function: Display entries in a table
# -------------------------------
def display_all(entries):
    """
    Prints all entries in a table format using tabulate.
    """
    if not entries:
        print("No entries found.")
        return

    headers = ["Date", "Type", "Category", "Amount", "Description"]
    print(tabulate(entries, headers=headers, tablefmt="grid"))


# Function: Filter entries by type or categeroy 
def filter_entries(entries, entry_type=None, category=None):
    """
    Filter entries by type (income/expense) or category.
    Returns a new list of filtered entries.
    """
    filtered = []

    for row in entries:
        row_type = row[1].lower()
        row_category = row[2].lower()
        if entry_type and row_type != entry_type.lower():
            continue
        if category and row_category != category.lower():
            continue
        filtered.append(row)

    return filtered



def show_summary(entries):
    """
    Calculate and display total income, total expense, and net balance.
    """
    total_income = 0
    total_expense = 0

    for row in entries:
        row_type = row[1].lower()
        amount = float(row[3])
        if row_type == "income":
            total_income += amount
        elif row_type == "expense":
            total_expense += amount

    net_balance = total_income - total_expense

    summary = [
        ["Total Income", total_income],
        ["Total Expense", total_expense],
        ["Net Balance", net_balance]
    ]

    print(tabulate(summary, headers=["Type", "Amount"], tablefmt="grid"))

def view_menu():
    """
    Display menu options for the user.
    """
    entries = load_entries()
    if not entries:
        return

    while True:
        print("\n--- VIEW ENTRIES MENU ---")
        print("1. View all entries")
        print("2. View only income")
        print("3. View only expenses")
        print("4. Filter by category")
        print("5. Show summary")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_all(entries)
        elif choice == "2":
            filtered = filter_entries(entries, entry_type="income")
            display_all(filtered)
        elif choice == "3":
            filtered = filter_entries(entries, entry_type="expense")
            display_all(filtered)
        elif choice == "4":
            cat = input("Enter category to filter: ")
            filtered = filter_entries(entries, category=cat)
            display_all(filtered)
        elif choice == "5":
            show_summary(entries)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")




if __name__ == "__main__":
    view_menu()
