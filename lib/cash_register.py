#!/usr/bin/env python3
  

from itertools import count


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
        self.dicount = discount
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

    

    
  pass
