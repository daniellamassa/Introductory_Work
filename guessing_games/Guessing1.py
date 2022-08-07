#this makes a simple guessing game

import random   #this allows for a random number generator


secretnumber = random.randint(0,10)
haveguessed = False

while (haveguessed == False):

    guessednumber = int(input("Pick a number from 0-10:"))

    if (guessednumber == secretnumber):
        print("Correct!")
        haveguessed = True
    elif (guessednumber > secretnumber):
        print("Too high.")
    elif (guessednumber < secretnumber):
        print("Too low.")

print("Game over.")
                        
