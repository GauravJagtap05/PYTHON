from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional


# Custom Exceptions
class BankException(Exception):
    """Base exception for bank operations"""
    pass


class InsufficientBalanceError(BankException):
    """Raised when account balance is insufficient"""
    pass


class AccountNotFoundError(BankException):
    """Raised when account is not found"""
    pass


class InvalidAmountError(BankException):
    """Raised when amount is invalid"""
    pass


class CustomerNotFoundError(BankException):
    """Raised when customer is not found"""
    pass


# Transaction Class
class Transaction:
    """Records a single transaction"""

    def __init__(self, transaction_type: str, amount: float, balance_after: float):
        self.transaction_type = transaction_type  # Deposit, Withdrawal, Transfer
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%d-%b')} | {self.transaction_type:12} | ₹{self.amount:8.2f} | Balance: ₹{self.balance_after:.2f}"


# Customer Class
class Customer:
    """Represents a bank customer"""
    _customer_id_counter = 1000

    def __init__(self, name: str, email: str):
        self.customer_id = f"C{Customer._customer_id_counter}"
        Customer._customer_id_counter += 1
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}"


# Abstract Account Class
class Account(ABC):
    """Abstract base class for bank accounts"""
    _account_counter = 1000

    def __init__(self, customer: Customer):
        self.account_number = f"ACC{Account._account_counter}"
        Account._account_counter += 1
        self.customer = customer
        self.balance = 0.0
        self.transactions = []

    @abstractmethod
    def calculate_interest(self) -> float:
        """Each account type calculates interest differently"""
        pass

    @abstractmethod
    def can_withdraw(self, amount: float) -> bool:
        """Each account has different withdrawal rules"""
        pass

    def deposit(self, amount: float) -> None:
        """Deposit money into account"""
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")

        self.balance += amount
        transaction = Transaction("Deposit", amount, self.balance)
        self.transactions.append(transaction)
        print(f"✓ Deposited ₹{amount} | New Balance: ₹{self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from account"""
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero")

        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Insufficient balance.\nAvailable: ₹{self.balance:.2f}, Requested: ₹{amount:.2f}"
            )

        if not self.can_withdraw(amount):
            raise InsufficientBalanceError(
                f"Withdrawal not allowed. Minimum balance required: ₹{self.get_minimum_balance():.2f}"
            )

        self.balance -= amount
        transaction = Transaction("Withdrawal", amount, self.balance)
        self.transactions.append(transaction)
        print(f"✓ Withdrew ₹{amount} | New Balance: ₹{self.balance:.2f}")

    def get_balance(self) -> float:
        """Get current balance (encapsulation)"""
        return self.balance

    def get_minimum_balance(self) -> float:
        """Override in subclass if needed"""
        return 0.0

    def display_transaction_history(self) -> None:
        """Display all transactions"""
        print(f"\n{'=' * 70}")
        print(f"Transaction History for {self.account_number}")
        print(f"{'=' * 70}")
        if not self.transactions:
            print("No transactions yet")
        else:
            for transaction in self.transactions:
                print(transaction)
        print(f"{'=' * 70}\n")

    def display_details(self) -> None:
        """Display account details"""
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Type: {self.__class__.__name__}")
        print(f"Customer: {self.customer.name}")
        print(f"Balance: ₹{self.balance:.2f}\n")


# Savings Account (Inheritance + Polymorphism)
class SavingsAccount(Account):
    """Savings account with minimum balance requirement"""
    MINIMUM_BALANCE = 1000.0
    INTEREST_RATE = 0.04  # 4% annual

    def calculate_interest(self) -> float:
        """Calculate interest for savings account"""
        return self.balance * self.INTEREST_RATE

    def can_withdraw(self, amount: float) -> bool:
        """Can only withdraw if minimum balance is maintained"""
        return (self.balance - amount) >= self.MINIMUM_BALANCE

    def get_minimum_balance(self) -> float:
        return self.MINIMUM_BALANCE


# Current Account (Inheritance + Polymorphism)
class CurrentAccount(Account):
    """Current account with no interest or minimum balance"""
    INTEREST_RATE = 0.0  # No interest

    def calculate_interest(self) -> float:
        """Current accounts don't earn interest"""
        return 0.0

    def can_withdraw(self, amount: float) -> bool:
        """Can withdraw any amount as long as balance exists"""
        return amount <= self.balance


# Bank Class (Main orchestrator)
class Bank:
    """Main bank class that manages customers and accounts"""

    def __init__(self, name: str):
        self.name = name
        self.customers = {}  # {customer_id: Customer}
        self.accounts = {}  # {account_number: Account}

    def create_customer(self, name: str, email: str) -> Customer:
        """Create a new customer"""
        customer = Customer(name, email)
        self.customers[customer.customer_id] = customer
        print(f"✓ Customer created: {customer}")
        return customer

    def create_account(self, customer_id: str, account_type: str) -> Account:
        """Create a new account for a customer"""
        if customer_id not in self.customers:
            raise CustomerNotFoundError(f"Customer {customer_id} not found")

        customer = self.customers[customer_id]

        if account_type.lower() == "savings":
            account = SavingsAccount(customer)
        elif account_type.lower() == "current":
            account = CurrentAccount(customer)
        else:
            raise ValueError("Account type must be 'savings' or 'current'")

        self.accounts[account.account_number] = account
        print(f"✓ {account_type.capitalize()} account created: {account.account_number}")
        return account

    def get_account(self, account_number: str) -> Account:
        """Get account by account number"""
        if account_number not in self.accounts:
            raise AccountNotFoundError(f"Account {account_number} not found")
        return self.accounts[account_number]

    def deposit(self, account_number: str, amount: float) -> None:
        """Deposit money into an account"""
        account = self.get_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number: str, amount: float) -> None:
        """Withdraw money from an account"""
        account = self.get_account(account_number)
        account.withdraw(amount)

    def transfer(self, from_account: str, to_account: str, amount: float) -> None:
        """Transfer money between accounts"""
        acc_from = self.get_account(from_account)
        acc_to = self.get_account(to_account)

        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be greater than zero")

        if amount > acc_from.get_balance():
            raise InsufficientBalanceError(f"Insufficient balance in {from_account}")

        # Perform transfer
        acc_from.balance -= amount
        acc_to.balance += amount

        # Record transactions
        acc_from.transactions.append(
            Transaction(f"Transfer To {to_account}", amount, acc_from.balance)
        )
        acc_to.transactions.append(
            Transaction(f"Transfer From {from_account}", amount, acc_to.balance)
        )

        print(f"✓ Transferred ₹{amount} from {from_account} to {to_account}")

    def display_bank_summary(self) -> None:
        """Display bank summary"""
        total_balance = sum(acc.get_balance() for acc in self.accounts.values())
        print(f"\n{'=' * 70}")
        print(f"🏦 {self.name} - Summary")
        print(f"{'=' * 70}")
        print(f"Total Customers: {len(self.customers)}")
        print(f"Total Accounts: {len(self.accounts)}")
        print(f"Total Bank Balance: ₹{total_balance:.2f}")
        print(f"{'=' * 70}\n")


# ============================================================================
# DEMO / TEST
# ============================================================================

if __name__ == "__main__":
    # Create bank
    bank = Bank("MyBank")

    # Create customers
    customer1 = bank.create_customer("Rahul Sharma", "rahul@email.com")
    customer2 = bank.create_customer("Priya Singh", "priya@email.com")

    # Create accounts
    acc1 = bank.create_account(customer1.customer_id, "savings")
    acc2 = bank.create_account(customer1.customer_id, "current")
    acc3 = bank.create_account(customer2.customer_id, "savings")

    print("\n" + "=" * 70)
    print("TESTING DEPOSITS")
    print("=" * 70)
    bank.deposit(acc1.account_number, 5000)
    bank.deposit(acc1.account_number, 3000)
    bank.deposit(acc2.account_number, 10000)
    bank.deposit(acc3.account_number, 2000)

    print("\n" + "=" * 70)
    print("TESTING WITHDRAWALS")
    print("=" * 70)
    bank.withdraw(acc1.account_number, 2000)
    bank.withdraw(acc2.account_number, 5000)

    print("\n" + "=" * 70)
    print("TESTING TRANSFERS")
    print("=" * 70)
    bank.transfer(acc1.account_number, acc3.account_number, 3000)

    print("\n" + "=" * 70)
    print("TESTING ERROR HANDLING")
    print("=" * 70)
    try:
        bank.withdraw(acc1.account_number, 10000)
    except InsufficientBalanceError as e:
        print(f"❌ Error: {e}")

    # Display transaction histories
    acc1.display_transaction_history()
    acc2.display_transaction_history()
    acc3.display_transaction_history()

    # Display account details
    acc1.display_details()

    # Display bank summary
    bank.display_bank_summary()

    # Test polymorphism (calculate interest)
    print("Testing Polymorphism - Interest Calculation:")
    print(f"Savings Account Interest: ₹{acc1.calculate_interest():.2f}")
    print(f"Current Account Interest: ₹{acc2.calculate_interest():.2f}")