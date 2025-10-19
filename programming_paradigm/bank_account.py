#!/usr/bin/python3
"""
Module: bank_account
Defines a BankAccount class to simulate basic banking operations.
"""

class BankAccount:
    """A simple BankAccount class that encapsulates deposit, withdrawal, and balance display."""

    def __init__(self, initial_balance=0.0):
        """
        Initialize the BankAccount with an optional initial balance.
        Args:
            initial_balance (float): Starting amount in the account. Defaults to 0.
        """
        self.__account_balance = float(initial_balance)  # Private attribute for encapsulation

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if sufficient funds exist.
        Args:
            amount (float): The amount to withdraw.
        Returns:
            bool: True if withdrawal succeeded, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
