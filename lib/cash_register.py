#!/usr/bin/env python3
  

class CashRegister:
  def __init__(self, discount=0):
    self.total = 0
    self.items = []
    self.previous_transactions = []
    self.discount = discount 
  
  @property
  def discount(self):
      return self._discount
    
  @discount.setter
  def discount(self, discount):
      if isinstance(discount, int) and 0 <= discount <= 100:
        self._discount = discount
      else:
        print("Not valid discount")
        self._discount = 0
  def add_item(self,item,price,quantity):
    self.total += price * quantity
    self.items.append(item)

    transaction = {
      "item": item,
      "price": price,
      "quantity": quantity
    }
    self.previous_transactions.append(transaction)

  def apply_discount(self):
    if len(self.previous_transactions) == 0:
      print("There is no discount to apply.")
    return
    self.total = self.total - (self.total * self.discount / 100)
  
  def void_last_transaction(self):
    if len(self.previous_transactions) == 0:
      return 
    
    last_transaction = self.previous_transactions.pop()

    item = last_transaction["item"]
    price = last_transaction["price"]
    quantity = last_transaction["quantity"]

    self.total -= price * quantity

    if item in self.items:
      self.items.remove(item)


    
  pass
