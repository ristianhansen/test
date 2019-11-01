# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:50:01 2019

@author: Christian
"""

"""
#Opgave 3.1 skriv en liste med navne og kald hvert navn ud fra position i liste


#Opgave 3.3 lav en liste med csgo hold, brug listen til at printe nogle statements.

navne = ['Michelle','Christian','Matt']
print(navne[0] + ",", navne[1] + ",", navne[2] + ".")
"""

"""
#Opgave 3.2  brug listen med navne igen, samtidig lav en variabel med en hilsen

navne = ['Michelle','Christian','Matt']
message = "Dejligt at se dig igen "
print("Hej", navne[0] + ",", message)
print("Hej", navne[1] + ",", message)
print("Hej", navne[2] + ",", message)
"""

"""
csgo = ['Asstralis','Heroic','NiP']
msg1 = "sutter røv i helvede"
msg2 = "det er ligesom at holde med AGF"
msg3 = "de gør det ok, men couldnt care less"

print(csgo[0], msg1 + "\n", csgo[1], msg2.lstrip() + "\n", csgo[2], msg3.lstrip() + ".")
"""

"""
#Opg. 3.4 lav en liste med gæster, brug herefter listen til at sende en personlig indbydelse til hver gæst.

guest = ['Christian','Matt','Michelle']
msg = "du er inviteret til fødselsdag"
print("Kære", guest[0], msg + ".")
print("Kære", guest[1], msg + ".")
print("Kære", guest[-1], msg, end="!")
"""

"""
#Opg. 3.5 Nogen kan ikke komme til festen, lav en print linje fra prg. 3.4 der skriver hvem der ikke kommer og tilføj nye til listen. print inv. igen.

guest = ['Christian','Matt','Michelle']
msg = "du er inviteret til fødselsdag"
print(guest)
print(guest[1], "kan desværre ikke komme alligevel.")
guest[1] = 'Jesper'
print(guest)
print("Kære", guest[0], msg + ".")
print("Kære", guest[1], msg + ".")
print("Kære", guest[-1], msg, end="!")
"""

"""
#Opg. 3.6 Inviter nogle flere gæster, brug insert() til at tilføje en ny gæst på plads 0, en i midten og append() for at tilføje i slutningen.

guest = ['Christian','Michelle','Matt']
print(guest)
print("Jeg har fundet et større bord, så der er plads til 3 gæster mere.")
guest.insert(0, 'kenned')
print(guest)
guest.insert(2, 'louise')
print(guest)
guest.append('Rosinen i pølseenden')
print(guest)
"""

"""
#Opg. 3.7 Bordet kommer ikke alligevel, brug pop() til at fjerne folk fra listen, send en besked til den der er blevet fjernet fra listen. brug del() til sidst.

guest = ['Christian','Michelle','Matt','Louise','Jesper']
print(guest)
uninvite1 = guest.pop(0)
print(uninvite1, "du er ikke inviteret mere")
print(guest)
uninvite2 = guest.pop(-1)
print(uninvite2, "du er ikke inviteret mere")
print(guest)
uninvite3 = guest.pop(2)
print(uninvite3, "du er ikke inviteret mere")
print(guest, "Tømmer listen nu")
guest.remove('Matt')
guest.remove('Michelle')
print(guest)
"""

"""

#Opgave 3.8 handler om at bruge sort(), sorted() og reverse() mht. lister.

byer = ['Danmark','Sverige','Holland','Kina','Indien']

print(byer)
byer.sort()
print(byer)
byer.reverse()
print(byer)
byer.reverse()
print(byer)
byer.sort(reverse=True)
print(byer)
byer.sort(reverse=False)
print(byer)
"""

"""
#Opg. 3.9 Brug len() til at printe hvor mange gæster der var inviteret i 3.4


guest = ['Christian','Matt','Michelle']
msg = "du er inviteret til fødselsdag"
print("Kære", guest[0], msg + ".")
print("Kære", guest[1], msg + ".")
print("Kære", guest[-1], msg + ".")
print("\nAntal inviterede gæster",len(guest))

"""

"""
#Opg. 3.10 lav en liste, og brug en af de introducerede funktioner i dette kapitel for hvert element.

csgo = ['Astralis','NiP','Heroic','Vitality','Evil Geniuses']
print(csgo)

csgo.insert(5, 'NaVi')
print(csgo)
skodhold = csgo.pop()
print(skodhold, "blev fjernet")
csgo.sort()
print(csgo)
csgo.sort(reverse=True)
print(csgo)
csgo.append('Renegades')
print(csgo)
csgo.remove('Renegades')
print(csgo)
csgo.sort(reverse=False)
print(csgo)
print(csgo[0], "Er pt. nr. 2 i verden")
"""




