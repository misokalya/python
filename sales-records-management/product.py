
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def to_list(self):
        return [self.product_id, self.name, self.price, self.quantity]

    def __str__(self):
        return f"{self.product_id} | {self.name} | Tsh {self.price:,.0f} | Stock: {self.quantity}"
