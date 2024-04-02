class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append({"type": "Income", "amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.balance -= amount
        self.transactions.append({"type": "Expense", "amount": amount, "description": description})

    def view_balance(self):
        return f"Your current balance is: ${self.balance}"

    def view_transactions(self):
        for index, transaction in enumerate(self.transactions, start=1):
            print(f"{index}. {transaction['type']}: {transaction['description']} (${transaction['amount']})")

    def run(self):
        while True:
            print("\n1. Add Income\n2. Add Expense\n3. View Balance\n4. View Transactions\n5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter income amount: "))
                description = input("Enter description: ")
                self.add_income(amount, description)
                print("Income added successfully.")

            elif choice == '2':
                amount = float(input("Enter expense amount: "))
                description = input("Enter description: ")
                self.add_expense(amount, description)
                print("Expense added successfully.")

            elif choice == '3':
                print(self.view_balance())

            elif choice == '4':
                self.view_transactions()

            elif choice == '5':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")


# Main function
if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()
