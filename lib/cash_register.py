#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []  # List to keep track of items
        self.last_transaction = 0  # To store the value of the last transaction

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)  # Add the item to the list based on quantity
        self.last_transaction = price * quantity  # Save the value of the last transaction

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            if self.total.is_integer():
                print(f"After the discount, the total comes to ${int(self.total)}.")
            else:
                print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Subtract the last transaction from the total."""
        self.total -= self.last_transaction
        # Reset the last transaction to ensure it's not used again
        self.last_transaction = 0
        # Optionally, you may want to remove the last item added from the items list as well
        if self.items:
            # Remove the last item added, based on how many were added
            self.items = self.items[:-1]

