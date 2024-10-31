# main.py

from bankLibrary import BankAccount

def chatbot():
    print("\n💬 Welcome to the Bank Chatbot!")
    print("Let's set up your account.")
    account = BankAccount(initial_balance=500)  # Initialize with a starting balance of $500
    
    print("\nHow can I assist you today? Type one of the commands to get started.\n")
    print("💸 Available commands: 'deposit', 'withdraw', 'balance', 'interest', 'history', 'exit'")
    print("=" * 50)

    while True:
        user_input = input("\nEnter your command: ").strip().lower()

        if user_input == "deposit":
            try:
                amount = float(input("Enter the amount to deposit: $"))
                print(account.deposit(amount))
            except ValueError:
                print("⚠️ Invalid amount. Please enter a number.")

        elif user_input == "withdraw":
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                print(account.withdraw(amount))
            except ValueError:
                print("⚠️ Invalid amount. Please enter a number.")

        elif user_input == "balance":
            print("=" * 50)
            print(account.get_balance())
            print("=" * 50)

        elif user_input == "interest":
            print("=" * 50)
            print(account.apply_interest())
            print("=" * 50)

        elif user_input == "history":
            print("=" * 50)
            print(account.print_transaction_history())
            print("=" * 50)

        elif user_input == "exit":
            print("🛑 Thank you for banking with us. Goodbye!")
            break

        else:
            print("❓ Sorry, I didn't understand that. Please try one of the available commands.")

if __name__ == "__main__":
    chatbot()