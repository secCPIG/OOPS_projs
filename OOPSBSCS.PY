class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: int, quantity: int,version: float):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.version = version

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity},{self.version})"

item1 = Item("Phone", 100, 1,2)
item2 = Item("Laptop", 1000, 3,4)
item3 = Item("Cable", 10, 5,6)
item4 = Item("Mouse", 50, 5,8)
item5 = Item("Keyboard", 75, 5,10)

print(item1)