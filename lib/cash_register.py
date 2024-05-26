#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  

    def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.total += item_cost
        self.items.extend([title] * quantity)
        self.last_transaction_amount = item_cost  

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction_amount
            self.items.pop()
            self.last_transaction_amount = 0 
        else:
            print("No transactions to void.")

    

