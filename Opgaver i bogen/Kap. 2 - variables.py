# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 13:49:39 2019

@author: Christian
"""

"""
#2.1. Simple Message: Assign a message to a variable, and then print that message.

message = 'Hello world, this is a short message service'
print(message)
"""
"""
#2.2 Simple message: assign a message to a variable, print it, change variable and print new message

message = "This is the first message"
print(message)
message = "this is the altered message"
print(message)
"""
"""
#2.3 use a variable to print persons name + greeting

fnavn = str(input("Skriv dit fornavn: "))
enavn = str(input("Skriv dit efternavn: "))
full = f"{fnavn.title()} {enavn.title()}"
print("Hej",full.title() +", velkommen til Python")
"""

"""
#2.4 use a variable to print a persons name in lower, upper and title

navn = str(input("Skriv dit navn her: "))
print(navn.lower())
print(navn.upper())
print(navn.title())
"""
"""
#2.5 find a fav. quote from an author, output should be autors name + once wrote: quote

vip = "Jeppe K"
citat = "ahahaha"

print(vip, "sagde engang:", citat.upper())
"""
"""
#2.6  remove whitespace from the input

navn = str(input("Skriv dit navn: "))

print(navn.strip())
"""
"""
#2.8 write a simple addition, subtraction, division, multiplication.

print(4+4)
print(8-0)
print(16/2)
print(2*4)
"""
"""
#2.9 use a variable to represent my fav. number - create a message that reveals my fav. number - print message + number

message = "Mit ynglingstal har altid været: "
tal = 7
print(f"{message}{tal}""!")
"""
