import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
        return []


def save_expenses(expenses):
    with open(FILE_NAME,  "W") as file:
        json.dump(expenses, file, indent=4)


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show Total Spending")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input ("Enter category: ")
            description = input("Enter description: ")


            try:
                amount = float(input("Enter amount: "))

                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue

            except ValueError:
                print("Please enter a valid number.")
                continue


            expense = {
                "category": category,
                "description": description,
                "amount": amount
            }

            expenses.append(expense)
            save_expenses(expenses)
            print("Expense saved successfully!")


        elif choice == "2":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                for number, expense in enumerate(expenses, start=1):
                    print(
                        number,
                        expense["category"],
                        expense["description"],
                        expense["amount"]
                    )

        elif choice == "3":
            total = sum(
                expense["amount"] for expense in expenses
            )

            print("Total spending:", round(total, 2))

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
