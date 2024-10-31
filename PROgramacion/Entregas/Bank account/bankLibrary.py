# bankLibrary.py

import random
from datetime import datetime

class BankAccount:
    def __init__(self, account_number=None, initial_balance=0, interest_rate=0.01):
        self.account_number = account_number if account_number else self._generate_account_number()
        self._balance = initial_balance
        self.interest_rate = interest_rate
        self.transaction_history = []
        print(f"🏦 Account {self.account_number} created with initial balance: ${self._balance:.2f}")

    def _generate_account_number(self):
        """Generates a unique 10-digit account number."""
        return str(random.randint(1000000000, 9999999999))

    def deposit(self, amount):
        if amount <= 0:
            return "⚠️ Deposit amount must be positive."
        self._balance += amount
        self._record_transaction("Deposit", amount)
        return f"✅ Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "⚠️ Withdrawal amount must be positive."
        if amount > self._balance:
            return "❌ Insufficient funds for this withdrawal."
        self._balance -= amount
        self._record_transaction("Withdrawal", amount)
        return f"✅ Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"

    def get_balance(self):
        return f"💰 Current Balance: ${self._balance:.2f}"

    def apply_interest(self):
        """Applies annual interest to the balance."""
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        return f"💸 Interest of ${interest:.2f} applied at a rate of {self.interest_rate * 100}%."

    def _record_transaction(self, transaction_type, amount):
        """Records a transaction with the current timestamp."""
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def print_transaction_history(self):
        """Returns the transaction history in a formatted way."""
        history = "\n📜 Transaction History:\n" + "=" * 40 + "\n"
        for transaction in self.transaction_history:
            history += f"{transaction['date']} | {transaction['type']: <10} | ${transaction['amount']:.2f}\n"
        history += "=" * 40
        return history