# Personal Finance Manager

A **GUI-based Python application** to track personal income and expenses. Manage your finances, view entries, and generate reports easily. Built with **Python** and **Tkinter**, beginner-friendly and extendable.

---

## Features

* **Add Entry**

  * **Type:** `income` or `expense`
  * **Category:** Income/Expense category (e.g., Food, Rent, Salary)
  * **Amount:** Numeric value of the entry
  * **Description:** Optional note
  * **Date & Time:** Auto-recorded

* **View Entries**

  * Displays all entries in a **scrollable table**
  * Columns: Date & Time, Type, Category, Amount, Description

* **Reports**

  * **Monthly Summary:** Total income and expenses per month
  * **Top Expense Categories:** Categories with highest spending
  * **Overall Summary:** Total income, expenses, and net balance

* **Easy-to-use GUI:** All features via Tkinter interface

---

## Installation

1. Clone repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:

```bash
pip install tabulate
```

> `tkinter` is included with Python.

3. Ensure **data/expenses.csv** exists (auto-created on first entry if missing)

---

## Usage

Run the GUI:

```bash
python main/main.py
```

* **Add Entry** – add new income or expense
* **View Entries** – see all transactions
* **Reports** – monthly, top categories, overall summaries

---

## Project Structure

```
project_root/
├── main/
│   └── main.py        # GUI entry point
├── modules/
│   ├── add_entry.py   # Add entries
│   ├── view_entries.py# Load/view entries
│   └── report.py      # Generate reports
├── data/
│   └── expenses.csv   # Transaction data
└── README.md
```

---

## Contributing

Contributions welcome! Add new features, improve GUI, or enhance reports via pull requests.

Ideas:

* Visual graphs
* Export reports to PDF/Excel
* Multi-user support
* Budgeting features

---

## License

Open-source. Use, modify, and share freely.


