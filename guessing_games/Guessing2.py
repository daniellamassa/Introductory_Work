#this makes a simple guessing game

import random   #this allows for a random number generator
import math

absolute2 = 0
secretnumber = random.randint(0,10)
haveguessed = False

   
while (haveguessed == False):

    guessednumber = int(input("Pick a number from 0-10:"))
   
    absolute1 = abs(guessednumber - secretnumber)
   
    if (guessednumber == secretnumber):
        print("Correct!")
        haveguessed = True
    elif (guessednumber != secretnumber):
        if absolute2 == 0:
            print("Wrong. Try again.")
            absolute2 = absolute1
        elif absolute1 < absolute2:
            print("Warmer.")
            absolute2 = absolute1
        else:
            print("Colder.")
            absolute2 = absolute1
print("Game over.")
    
