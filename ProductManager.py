class ProductManager:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def calculateDiscount(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)