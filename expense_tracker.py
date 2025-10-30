import csv

FILENAME = "expenses.csv"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = float(input("Enter amount spent: "))

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added successfully!\n")

def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            total = 0
            print("\n Expense Records:")
            print("-" * 35)
            for row in reader:
                print(f"Date: {row[0]} | Category: {row[1]} | Amount: ₹{row[2]}")
                total += float(row[2])
            print("-" * 35)
            print(f"Total Spent: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

def main():
    print("Personal Expense Tracker")
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye! Stay on budget.")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
