import csv
import datetime
import os

# -------------------------------
# Function to add entry to CSV
# -------------------------------
def add_entry(entry_type, category, amount, description):
    base_dir = os.path.dirname(os.path.dirname(__file__))  # project root
    csv_path = os.path.join(base_dir, "data", "expenses.csv")

    get_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = [get_date, entry_type, category, amount, description]

    with open(csv_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# -------------------------------
# Optional CLI for testing
# -------------------------------
def get_entry():
    entry_type = input("Enter type (income/expense): ").lower()
    while entry_type not in ["income", "expense"]:
        entry_type = input("Invalid type. Enter again (income/expense): ").lower()

    category = input("Enter category: ")
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than 0")
                continue
            break
        except ValueError:
            print("Invalid amount. Enter a number.")

    description = input("Enter description: ")

    return entry_type, category, amount, description


if __name__ == "__main__":
    entry_type, category, amount, description = get_entry()
    add_entry(entry_type, category, amount, description)
    print("Entry added successfully!")
