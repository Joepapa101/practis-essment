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


while True:
    combo_meals = {}
    combomeal = enterbox('enter the name of the combo meal')
    combo_meals
    firstcombo = enterbox('enter the name of the first combo, format name:price')
    secondcombo = enterbox('enter the name of the second combo')
    thirdcombo = enterbox('enter the name of the third item')

    combo_meals[combomeal] = {
        'burger': {'name': firstcombo.split(':')[0], 'price': float(firstcombo.split(':')[1])},
        'fries': {'name': secondcombo.split(':')[0], 'price': float(secondcombo.split(':')[1])},
        'drink': {'name': thirdcombo.split(':')[0], 'price': float(thirdcombo.split(':')[1])}
    }
    buttonbox(combomeal, choices= ['edit', 'back to menu'])