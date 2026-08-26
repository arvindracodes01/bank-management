"""
SIMPLE BANK MANAGEMENT SYSTEM

"""

# ---------------------------------------------------
# A simple class to represent a bank account
# ---------------------------------------------------
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def show_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")


# ---------------------------------------------------
# Dictionary to store all accounts
# key = account number, value = BankAccount object
# ---------------------------------------------------
accounts = {}
next_account_number = 1  # simple counter for account numbers


# ---------------------------------------------------
# Function to create a new account
# ---------------------------------------------------
def create_account():
    global next_account_number

    name = input("Enter your name: ")

    # Loop until user enters a valid starting amount
    while True:
        try:
            starting_balance = float(input("Enter starting deposit amount: "))
            if starting_balance < 0:
                print("Amount cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    new_account = BankAccount(name, starting_balance)
    accounts[next_account_number] = new_account

    print(f"\nAccount created successfully!")
    print(f"Your account number is: {next_account_number}\n")

    next_account_number = next_account_number + 1


# ---------------------------------------------------
# Function to deposit money
# ---------------------------------------------------
def deposit_money():
    try:
        acc_no = int(input("Enter your account number: "))

        if acc_no not in accounts:
            print("Account not found.\n")
            return

        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount must be greater than zero.\n")
            return

        accounts[acc_no].deposit(amount)
        print("Deposit successful!")
        accounts[acc_no].show_balance()
        print()

    except ValueError:
        print("Invalid input. Please enter numbers only.\n")


# ---------------------------------------------------
# Function to withdraw money
# ---------------------------------------------------
def withdraw_money():
    try:
        acc_no = int(input("Enter your account number: "))

        if acc_no not in accounts:
            print("Account not found.\n")
            return

        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount must be greater than zero.\n")
            return

        # Check if enough balance is available
        if amount > accounts[acc_no].balance:
            print("Insufficient balance!\n")
            return

        accounts[acc_no].withdraw(amount)
        print("Withdrawal successful!")
        accounts[acc_no].show_balance()
        print()

    except ValueError:
        print("Invalid input. Please enter numbers only.\n")


# ---------------------------------------------------
# Function to check balance
# ---------------------------------------------------
def check_balance():
    try:
        acc_no = int(input("Enter your account number: "))

        if acc_no not in accounts:
            print("Account not found.\n")
            return

        accounts[acc_no].show_balance()
        print()

    except ValueError:
        print("Invalid input. Please enter a valid account number.\n")


# ---------------------------------------------------
# Function to show all accounts (uses a for loop)
# ---------------------------------------------------
def show_all_accounts():
    if len(accounts) == 0:
        print("No accounts yet.\n")
        return

    print("\n--- All Accounts ---")
    for acc_no in accounts:
        account = accounts[acc_no]
        print(f"Acc No: {acc_no} | Name: {account.name} | Balance: {account.balance}")
    print()


# ---------------------------------------------------
# Main program - shows menu in a loop
# ---------------------------------------------------
def main():
    while True:
        print("===== BANK MENU =====")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Show All Accounts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        print()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            show_all_accounts()
        elif choice == "6":
            print("Thank you for using the Bank System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.\n")


# Start the program
main()