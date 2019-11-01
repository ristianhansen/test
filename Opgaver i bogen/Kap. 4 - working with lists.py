"""
#Opg. 4.1 - make a list whith 3 pizzas, make for loop to present each one

pizzaer = ['Pepperoni','Hawaii','Calzone']

for pizza in pizzaer:
    print("Jeg elsker en", f"{pizza}", "pizza.")

print("\nJeg elsker pizza", "\nDen er virkelig lækker", "\nSuper dejlig pizza")
"""


"""
#Opg 4.2 - make a list with 3 animals, use for loop to present each animal.

animals = ['Ko','Gris','Kylling']

for animal in animals:
    print("En", f"{animal.lower()}", "er velegnet til slagtning")
    
print("\nAlle disse dyr smager fantastisk tilberedt :-)")
"""

"""
#printer fra 1-10
numbers = list(range(1,11))
print(numbers)

#printer alle ulige tal fra 1-9 
numbers = list(range(1,11,2))
print(numbers)

#printer de første 10 kvadratrøder
squares = []

for value in range(1,11):
    squares.append(value ** 2)
    
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
"""

"""
#Opg. 4.3 - use a loop to print the numbers from 1-20

tal = list(range(1,21))
for nummer in tal:
    print(nummer)
"""

"""
#Opg. 4.4 - use min(), max() & sum() and a range 1-1000000 to see how quick python is.

tal = list(range(1,1000000))
print(min(tal))
print(max(tal))
print(sum(tal))
"""

"""
#Opg. 4.5 - odd numbers. make a list from 1-20 and print the odd numbers in a loop

tal = list(range(1,21,2))

for nummer in tal:
    print(nummer)
"""

"""
#Opg. 4.7 - make a list of the multiplies of 3 from 3 - 30  use a for loop.

tal = list(range(3,33,3))

for nummer in tal:
    print(nummer)
"""

"""
#Opg. 4.8 - a number raised to the third power is called a cube ex 2**3 make 10 first cubes.

tal = []

for value in range(1,11):
    tal.append(value ** 3)
print(tal)
"""

"""
#Opg. 4.9 - use list comprehension to make a list of the 10 first cubes.

tal = [value ** 3 for value in range(1,11)]
print(tal)
"""

"""
#Opg. 4.10 - Make a list with several names, then slice elements out.

tal = list(range(1,26))

print(tal)

print("De første 3 tal på listen er", tal[0:3])
print("De 3 mellemste tal på listen er", tal[14], tal[15], tal[16])
print("De sidste 3 tal på listen er", tal[22:])
"""

"""
#Opg. 4.11 - Copy af list to a new list.

pizzaer = ['Pepperoni','Hawaii','Calzone']
print(pizzaer)

pizza2 = pizzaer[:]
print(pizzaer)

pizzaer.append('Skinkedyret')
print(pizzaer)

pizza2.append('Quadro fromagio')
print(pizza2)

print("Min ynglings pizzaer er", f"{pizzaer}")
print("Den anden liste med pizzaer er ikke lige mig", f"{pizza2}")
"""
"""
#Opg. 4.12 - for loops. skriv min 2 for loops.

pizzaer = ['Pepperoni','Magarita','Hawaii','Calzone']

for pizza in pizzaer:
    print(pizza)
    
pizzaer.append('Skinkedyret')
pizzaer.pop(1)
print(pizzaer)



tal = list(range(7,77,7))

for nummer in tal:
    print(nummer)
"""

# TUPPLE ER EN LISTE SOM IKKE KAN ÆNDRES!!! skrives som tuppel = (ting i tupplen) hvis der kun er et element skriv: (3,)
# En tupple kan gendefineres så hvis man skriver samme navn = (ny værdi,)

"""
#Opg. 4.13 - make a tupple with min. 5 items. make a for loop to print the itemds.


mad = ('æble', 'pære', 'banan', 'jordbær', 'kiwi')

for vare in mad:
    print(vare)

# mad[0] = 'citron' uncomment af denne linje vil medføre fejl, da man ikke kan assigne en ny værdi i tupplet.
print("\nDen nye menu:")   
mad = ('appelsin', 'papaya', 'banan', 'jordbær', 'kiwi') # denne linje gendefinere tuppletten med nye elementer

for vare in mad:
    print(vare)

""" 










