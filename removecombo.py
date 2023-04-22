from easygui import *


combo_meals = {
    'Beef Burger Combo': {
        'burger': {'name': 'Beef Burger', 'price': 4.69},
        'fries': {'name': 'Regular Fries', 'price': 1.00},
        'drink': {'name': 'Fizzy Drink', 'price': 1.00}
    },
    'Cheezeburger Combo': {
        'burger': {'name': 'Cheezeburger', 'price': 5.69},
        'fries': {'name': 'Regular Fries', 'price': 1.00},
        'drink': {'name': 'Fizzy Drink', 'price': 1.00}
       
    },
    'Super Combo': {
        'burger': {'name':'Cheeseburger', 'price': 8.69},
        'fries': {'name': 'Large Fries', 'price': 2.00},
        'drink': {'name': 'Smoothie', 'price': 2.99}
        
    
    }
}





remove_combo = enterbox('enter the combo you are going to remove')
del combo_meals[remove_combo]
print(combo_meals)