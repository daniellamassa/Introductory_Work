#Programmers: Dani and Madelyn

#This function takes a string, and returns the
#number of times the character 'e' appears in the string.

def CountEs(word):
    counter = 0
    for letter in word:
        if letter == 'e':
            counter += 1
    return counter

#This function takes a  given string, and returns the
#total number of vowels that appear in the string.

def CountVowels(word):
    AllVowels =  ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for letter in word:
        if letter in AllVowels:
            counter += 1
    return counter

#This function take given string, and returns the string reversed.

def ReverseString(word):
    l = list(word)
    Reverse = l[-1::-1]
    stringReverse = ''
    for letter in Reverse:
        stringReverse = stringReverse + letter
    return stringReverse

#This function takes a given string, and returns a list of the vowels
#found in the string

def FindVowels(word):
    AllVowels =  ['a', 'e', 'i', 'o', 'u']
    List = []
    for letter in word:
        if letter in AllVowels:
            List.append(letter)
    return List
    
        
    
    
    
