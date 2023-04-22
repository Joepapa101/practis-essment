from easygui import *

#combo meals dictionary
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




#main code
def menu_options():
    choices = buttonbox('What would you like to do', choices=['Add Combo', 'Remove Combo', 'Find Combo', 'Output Combos', 'Exit'])
    if choices == 'Add Combo':
        add_combo(combo_meals)
    elif choices == 'Remove Combo':
        remove_combo(combo_meals)
    elif choices == 'Find Combo':
        find_combo(combo_meals)
    elif choices == 'Output Combos':
        output_combos()
    elif choices == 'Exit':
        exit()


def add_combo(combo_meals):
    #loop so if the person corrects their entries it won't skip back on the menu
    while True:
        combomeal = enterbox('Enter the name of the meal combo')
        firstcombo = enterbox('Enter the name of the First item, Format name:price')
        secondcombo = enterbox('enter the name of the second item, Format name:price')
        thirdcombo = enterbox('Enter the name of the third item, format name:price')
        #new dictionary entry (Since I told the user to enter name and price in the same textbox, I seperated the name and price with a : and split them as appropriate)
        combo_meals[combomeal] = {
            'burger': {'name': firstcombo.split(':')[0], 'price': float(firstcombo.split(':')[1])},
            'fries': {'name': secondcombo.split(':')[0], 'price': float(secondcombo.split(':')[1])},
            'drink': {'name': thirdcombo.split(':')[0], 'price': float(thirdcombo.split(':')[1])}
        }
        buttonbox(combo_meals[combomeal], choices= ['edit', 'back to menu'])

        print(combo_meals)
        menu_options()



def remove_combo(combo_meals):
    remove_combo = enterbox('enter the combo you are going to remove')
    del combo_meals[remove_combo]
    print(combo_meals)
    menu_options()


def find_combo(combo_meals):
    combo = enterbox('Search any particular combo')
    if combo in combo_meals:
        #this got a bit funky to program
        msgbox(f"The {combo}combo exists")
        menu_options()
    else:
        msgbox(f'The combo {combo} does not exist.')
        menu_options()


def output_combos():
    print(combo_meals)
    msgbox('Success! The combo meals have been printed! Check the console.')
    menu_options()


#main_code I guess
menu_options()
