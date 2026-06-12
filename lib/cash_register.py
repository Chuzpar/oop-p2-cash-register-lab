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
  pass
