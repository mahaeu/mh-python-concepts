"""
Interactive example: Bank account with separated responsibilities.

This script demonstrates:
- a class as a blueprint
- an object as a long-lived instance
- methods modifying object state
- a second class handling business rules

Run this file and interact with the account via the terminal.
"""


class InterestPolicy:
    def __init__(self, rate: float):
        self.rate = rate

    def calculate_interest(self, balance: float) -> float:
        return balance * self.rate


class BankAccount:
    currency = "EUR"

    def __init__(self, owner: str, policy: InterestPolicy):
        self.owner = owner
        self.balance = 0.0
        self.policy = policy

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        self.balance -= amount

    def apply_interest(self) -> None:
        interest = self.policy.calculate_interest(self.balance)
        self.balance += interest


# ------------------------------------------------------------
# Interactive program
# ------------------------------------------------------------

if __name__ == "__main__":
    policy = InterestPolicy(rate=0.02)
    account = BankAccount(owner="You", policy=policy)

    print("Bank account started")
    print("--------------------")

    while True:
        print(f"\nCurrent balance: {account.balance:.2f} {BankAccount.currency}")
        print("Choose action: deposit | withdraw | interest | show | quit")

        action = input("> ").strip().lower()

        if action == "deposit":
            amount = float(input("Amount to deposit: "))
            account.deposit(amount)

        elif action == "withdraw":
            amount = float(input("Amount to withdraw: "))
            account.withdraw(amount)

        elif action == "interest":
            account.apply_interest()
            print("Interest applied")

        elif action == "show":
            print(f"Balance: {account.balance:.2f} {BankAccount.currency}")

        elif action == "quit":
            print("Goodbye")
            break

        else:
            print("Unknown action")
