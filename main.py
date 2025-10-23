import tkinter as tk
from tkinter import ttk, messagebox
from modules.add_entry import add_entry
from modules.view_entries import load_entries
from modules.report import monthly_summary, top_expense_categories, overall_summary
import io, sys

# -------------------------------
# GUI Functions
# -------------------------------
def open_add_entry():
    add_win = tk.Toplevel(root)
    add_win.title("Add Entry")
    add_win.geometry("350x300")

    tk.Label(add_win, text="Type (income/expense):").pack(pady=5)
    type_entry = tk.Entry(add_win)
    type_entry.pack()

    tk.Label(add_win, text="Category:").pack(pady=5)
    category_entry = tk.Entry(add_win)
    category_entry.pack()

    tk.Label(add_win, text="Amount:").pack(pady=5)
    amount_entry = tk.Entry(add_win)
    amount_entry.pack()

    tk.Label(add_win, text="Description:").pack(pady=5)
    desc_entry = tk.Entry(add_win)
    desc_entry.pack()

    def submit():
        entry_type = type_entry.get().strip().lower()
        category = category_entry.get().strip()
        description = desc_entry.get().strip()
        try:
            amount = float(amount_entry.get().strip())
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number")
            return

        if entry_type not in ["income", "expense"]:
            messagebox.showerror("Invalid Input", "Type must be 'income' or 'expense'")
            return

        add_entry(entry_type, category, amount, description)
        messagebox.showinfo("Success", "Entry added successfully!")
        add_win.destroy()

    tk.Button(add_win, text="Submit", command=submit).pack(pady=10)

# -------------------------------
def open_view_entries():
    entries_win = tk.Toplevel(root)
    entries_win.title("View Entries")
    entries_win.geometry("700x400")

    entries = load_entries()
    if not entries:
        tk.Label(entries_win, text="No entries found.").pack()
        return

    columns = ("Date", "Type", "Category", "Amount", "Description")
    tree = ttk.Treeview(entries_win, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=120)
    for row in entries:
        tree.insert("", tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)
    scrollbar = ttk.Scrollbar(entries_win, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# -------------------------------
# Reports GUI
# -------------------------------
def open_reports():
    report_win = tk.Toplevel(root)
    report_win.title("Reports")
    report_win.geometry("300x250")

    tk.Button(report_win, text="Monthly Summary", width=25, command=show_monthly_summary).pack(pady=10)
    tk.Button(report_win, text="Top Expense Categories", width=25, command=show_top_expenses).pack(pady=10)
    tk.Button(report_win, text="Overall Summary", width=25, command=show_overall_summary).pack(pady=10)

# -------------------------------
# Capture report print output
# -------------------------------
def capture_report(func):
    entries = load_entries()
    if not entries:
        messagebox.showinfo("Report", "No entries found.")
        return
    buffer = io.StringIO()
    sys.stdout = buffer
    func(entries)
    sys.stdout = sys.__stdout__
    messagebox.showinfo("Report", buffer.getvalue())

def show_monthly_summary():
    capture_report(monthly_summary)

def show_top_expenses():
    capture_report(top_expense_categories)

def show_overall_summary():
    capture_report(overall_summary)

# -------------------------------
# Main GUI Window
# -------------------------------
root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("300x300")

tk.Label(root, text="PERSONAL FINANCE MANAGER", font=("Helvetica", 14, "bold")).pack(pady=20)

tk.Button(root, text="Add Entry", width=25, command=open_add_entry).pack(pady=10)
tk.Button(root, text="View Entries", width=25, command=open_view_entries).pack(pady=10)
tk.Button(root, text="Reports", width=25, command=open_reports).pack(pady=10)
tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=10)

root.mainloop()
