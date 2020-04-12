from menu_item import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def info(self):
        return f'{self.name}: ₹{self.price} ({self.volume} mL)'
