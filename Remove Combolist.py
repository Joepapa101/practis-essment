from easygui import *

comboname = ['cheesy pleaser']
comboprice = ['1']

entryname = enterbox("""Enter the name of the item you would like to delete.  
                          You do not have to include price, however if you do, 
                          ensure you stick to the correct formatting name:price""")

comboname.remove(entryname.split(':')[0])
comboprice.remove(entryname.split(':')[1])

print(comboname)
print(comboprice)



