import random
from datetime import datetime, timedelta

class BankAccount:
    def __init__(self, account_number=None, initial_balance=0, interest_rate=0.01):
        self.account_number = account_number if account_number else self._generate_account_number()
        self._balance = initial_balance
        self.interest_rate = interest_rate  # Annual interest rate
        self.transaction_history = []
        print(f"Account {self.account_number} created with initial balance: ${self._balance:.2f}")

    def _generate_account_number(self):
        """Generates a unique 10-digit account number."""
        return str(random.randint(1000000000, 9999999999))

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        self._record_transaction("Deposit", amount)
        print(f"✅ Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self._balance:
            print("❌ Insufficient funds.")
            return
        self._balance -= amount
        self._record_transaction("Withdrawal", amount)
        print(f"✅ Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")

    def get_balance(self):
        return self._balance

    def apply_interest(self):
        """Applies annual interest to the balance."""
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"💰 Interest of ${interest:.2f} applied at rate {self.interest_rate * 100}%.")

    def _record_transaction(self, transaction_type, amount):
        """Records a transaction with the current timestamp."""
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def print_transaction_history(self):
        """Prints the transaction history in a formatted way."""
        print("\nTransaction History:")
        print("-" * 40)
        for transaction in self.transaction_history:
            print(f"{transaction['date']} | {transaction['type']: <10} | ${transaction['amount']:.2f}")
        print("-" * 40)

    def __str__(self):
        return f"BankAccount({self.account_number}), Balance: ${self._balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number=None, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, initial_balance, interest_rate)

    def estimate_interest(self, months):
        """Estimates interest generated for the specified number of months."""
        monthly_rate = self.interest_rate / 12
        future_balance = self._balance * ((1 + monthly_rate) ** months)
        estimated_interest = future_balance - self._balance
        print(f"💸 Estimated interest for {months} months: ${estimated_interest:.2f}")
        return estimated_interest


class CheckingAccount(BankAccount):
    def __init__(self, account_number=None, initial_balance=0, overdraft_limit=500):
        super().__init__(account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        """Allows overdraft up to the specified limit."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self._balance + self.overdraft_limit:
            print("❌ Insufficient funds. Overdraft limit exceeded.")
            return
        self._balance -= amount
        self._record_transaction("Withdrawal", amount)
        print(f"✅ Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")


# Main Program with User Input
def main():
    # Create a savings and a checking account
    savings_account = SavingsAccount(initial_balance=1000)
    checking_account = CheckingAccount(initial_balance=500)

    while True:
        # Display options to the user
        print("\n--- Bank Account Menu ---")
        print("1. Deposit to Savings")
        print("2. Withdraw from Savings")
        print("3. Estimate Savings Interest")
        print("4. Deposit to Checking")
        print("5. Withdraw from Checking")
        print("6. Check Balance for Savings and Checking")
        print("7. Apply Interest to Savings")
        print("8. View Transaction History")
        print("9. Exit")

        # Get user's choice
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit in savings: "))
            savings_account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw from savings: "))
            savings_account.withdraw(amount)

        elif choice == "3":
            months = int(input("Enter the number of months to estimate interest: "))
            savings_account.estimate_interest(months)

        elif choice == "4":
            amount = float(input("Enter amount to deposit in checking: "))
            checking_account.deposit(amount)

        elif choice == "5":
            amount = float(input("Enter amount to withdraw from checking: "))
            checking_account.withdraw(amount)

        elif choice == "6":
            print(f"\nSavings Balance: ${savings_account.get_balance():.2f}")
            print(f"Checking Balance: ${checking_account.get_balance():.2f}")

        elif choice == "7":
            savings_account.apply_interest()

        elif choice == "8":
            print("\n--- Savings Account History ---")
            savings_account.print_transaction_history()
            print("\n--- Checking Account History ---")
            checking_account.print_transaction_history()

        elif choice == "9":
            print("Thank you for using the bank account system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 9.")

if __name__ == "__main__":
    main()