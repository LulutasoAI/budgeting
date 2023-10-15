import matplotlib.pyplot as plt

def create_budget_pie_chart(budget):
    names = list(budget.keys())
    amounts = list(budget.values())

    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=names, autopct='%1.1f%%', startangle=140)
    plt.title('Budget Allocation')

    plt.axis('equal')  
    plt.show()

budget = {
    "Food": 500,
    "Rent": 1000,
    "Transportation": 300,
    "Entertainment": 200,
}
print(sum(budget.values()))
create_budget_pie_chart(budget)
