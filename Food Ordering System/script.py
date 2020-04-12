from food import Food
from drink import Drink

food1 = Food('Sandwich', 60, 330)
food2 = Food('Chocolate Cake', 40, 450)
food3 = Food('Cream Puff', 20, 180)

foods = [food1, food2, food3]

drink1 = Drink('Coffee', 40, 180)
drink2 = Drink('Orange Juice', 30, 350)
drink3 = Drink('Espresso', 30, 250)

drinks = [drink1, drink2, drink3]

print('Foods')
for index,food in enumerate(foods, start=1):
    print(f'{index}. {food.info()}')

print('Drinks')
for index, drink in enumerate(drinks, start=1):
    print(f'{index}. {drink.info()}')

print('-------------------------')

food_order = int(input('Enter food item number: '))
selected_food = foods[food_order-1]

drink_order = int(input('Enter drink item number: '))
selected_drink = drinks[drink_order-1]

print(f'Your meal: {selected_food.name} and {selected_drink.name}')

count = int(input('How many meals would you like to purchase? (10% off for 3 or more): '))
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)
print(f'Your total is ₹{result}')
