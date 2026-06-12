class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity

        for i in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            return

        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]

        for i in range(last["quantity"]):
            if last["title"] in self.items:
                self.items.remove(last["title"])

        if self.total < 0:
            self.total = 0.0