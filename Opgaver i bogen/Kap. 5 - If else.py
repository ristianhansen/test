# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 06:16:45 2019

@author: Christian
"""
"""
#Basic if statement inside a for loop.

csgo = ['nip','astralis','heroic','navi']

for cs in csgo:
    if cs == 'nip':
        print(cs.upper())
    else:
        print(cs)
"""

# checking for equality "==", checking for unequality "!=", testing 2 conditions brug and (begge skal være true) eller or hvis kun en af de to 
# skal være true.
# to see if a value is in the list use "in" 

"""

#Basic if statement checking for unequality.

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies")
"""

"""
#Checking if value ristian is in the list.

banned_users = ['c00land','pip','guldand']

user = 'ristian'

if user not in banned_users:
    print(f"{user.title()}", "du er selvfølgelig ikke banned")
"""


"""
#Opg. 5.1 Conditional tests. // true or false statements. + Opg. 5.2 skriv min. 10 øvelser med tue false.

csgo = 'NiP'

print("Er csgo holdet == 'NiP' ? så er det true")
print(csgo == 'NiP')
print("Er csgo holdet == 'asstralis' ? Så er det false")
print(csgo == 'asstrallis')

bil = 'Audi'
print(bil == 'bmw')
print(bil == 'Audi')
print(bil.lower() == 'audi')



toppings = 'ost'
if toppings == 'ost':
    print("Dette statement er true")
if toppings != 'svampe':
    print("False, men lad os spise dem alligevel")


biler = ['Mercedes','Audi','BMW']

for bil in biler:
    if bil == 'Audi':
        print("Das ist korrekt!")
    else:   
        print(bil == 'skoda')
        
"""