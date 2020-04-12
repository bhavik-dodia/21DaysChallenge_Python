from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        super().__init__(name, price)
        self.calorie_count = calorie_count
    
    def info(self):
        return f'{self.name}: ₹{self.price} ({self.calorie_count} kcal)'
