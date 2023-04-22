import easygui

comboname = []
comboprice = []

addcombo = easygui.enterbox('Enter the name and the price of the combo in the format name:price')

comboname.append(addcombo.split(':')[0])
comboprice.append(addcombo.split(':')[1])

print(comboname)
print(comboprice)


