#Programmers: Dani and Madelyn

# This function takes a given string and a shift amount,
# and returns a new string that has been shifted.

def ShiftCypher(word, shift):
    string = ''
    for letter in word:
        letter = ord(letter)
        NewLetter = letter + shift
        NewLetter = chr(NewLetter)
        string = string + NewLetter
    return string
