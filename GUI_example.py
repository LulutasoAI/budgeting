import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class BudgetPieChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Pie Chart")

        self.budget_entries = []
        self.row = 1

        add_entry_button = tk.Button(root, text="Add Budget Entry", command=self.add_budget_entry)
        add_entry_button.grid(row=0, column=1)

        submit_button = tk.Button(root, text="Submit Budget", command=self.submit_budget)
        submit_button.grid(row=0, column=2)

    def create_budget_pie_chart(self, budget):
        names = list(budget.keys())
        amounts = list(budget.values())

        plt.figure(figsize=(8, 8))
        plt.pie(amounts, labels=names, autopct='%1.1f%%', startangle=140)
        plt.title('Budget Allocation')

        plt.axis('equal')  
        plt.show()

    def submit_budget(self):
        budget = {}
        for entry in self.budget_entries:
            name = entry['name'].get()
            amount = entry['amount'].get()
            if name and amount:
                budget[name] = float(amount)

        if budget:
            self.create_budget_pie_chart(budget)
        else:
            messagebox.showerror("Error", "Please enter budget items and amounts.")

    def add_budget_entry(self):
        entry = {
            "name": tk.StringVar(),
            "amount": tk.StringVar()
        }

        name_label = tk.Label(self.root, text="Name:")
        name_label.grid(row=self.row, column=0)
        name_entry = tk.Entry(self.root, textvariable=entry["name"])
        name_entry.grid(row=self.row, column=1)

        amount_label = tk.Label(self.root, text="Amount:")
        amount_label.grid(row=self.row, column=2)
        amount_entry = tk.Entry(self.root, textvariable=entry["amount"])
        amount_entry.grid(row=self.row, column=3)

        self.budget_entries.append(entry)
        self.row += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetPieChartApp(root)
    root.mainloop()
