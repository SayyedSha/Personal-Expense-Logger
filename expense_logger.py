import csv
from datetime import datetime

file_name = "expenses.csv"

try:
    with open(file_name, mode='x', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Note"])
except FileExistsError:
    pass

def add_expense():
    category = input("Enter category (e.g., food, transport): ")
    amount = input("Enter amount: ")
    note = input("Add a short note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully!\n")

def add_expense():
    category = input("Enter category (e.g., food, transport): ")
    amount = input("Enter amount: ")
    note = input("Add a short note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("✅ Expense added successfully!\n")

def view_expenses():
    print("\n📄 All Logged Expenses:\n")
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    print()

def view_summary():
    total = 0.0
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[2])
    print(f"\n💰 Total Spent: ₹{total:.2f}\n")

while True:
    print("------ Personal Expense Logger ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        print("👋 Goodbye! Keep saving!")
        break
    else:
        print("❌ Invalid choice. Try again.\n")