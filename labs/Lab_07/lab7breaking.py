#Programmer: Dani Massa
#Artist: Rick Astley

#This function takes a given a string and letter, and returns the
#number of times the letter occurs in the string.

def CountLetter(word, letter):
    counter = 0
    for item in word:
        if item == letter:
            counter += 1
    return counter

#This function takes a given string, and returns a dictionary whose
#keys are the lower case letters, and whose values are the letter
#counts for those letters.

def LetterCounts(word):
    Dict = {}
    for item in word:
        counter = CountLetter(word, item)
        if item == item.lower():
            Dict[item] = counter
    return Dict

#This function takes a given string message (msg) and a substitution
#dictionary (subdict), and performs a substitution cypher on the message.
#The keys of the dictionary are the unscrambled letters, and the values
#are their corresponding scramble.

def SubCypher(msg, subdict):
    NewString = ""
    for item in msg:
        if (item in subdict):
            value = subdict[item]
            NewString = NewString + value
        else:
            NewString = NewString + item
    return NewString


#This dictionary unscrables the given message.
subdict = {'p':'I', 'o':'M', 'r':'E', 'h':'A', 'v':'W', 'w':'R',
           'x':'N', 'e':'O', 'm':'S', 'j':'T', 'g':'G', 'm':'S',
           'k':'L', 'z':'V', 'd':'Y', 'u':'U', 'i':'K', 'y':'H',
           'l':'D', 't':'F', 's':'C', 'b':'J', 'q':'P', 'a':'B',}

