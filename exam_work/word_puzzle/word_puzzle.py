# Programmer: Dani Massa

'''
algorithm for solving task:
First, create a helper function that returns a string of all the vowels, and
only the vowels from a given word. Use this helper function within the
mystery_words function. Call the helper function on every word in the
get_wordlist(). Then, check to see if the remaining vowels of each word is
equal to 'aeiou', in that order. If so, append the entire word to an empty list.    
'''

from wordlist import get_wordlist

# Note: calling the function get_wordlist returns a (pretty big) list
# of English words. Do not try to print the whole list.

def helper(word):
    vowels = 'aeiou'
    NewString = ''
    for item in word:
        if item in vowels:
            NewString = NewString + (item)
    return (NewString)
            
def mystery_words():
    List = []
    vowels = 'aeiou'
    for item in get_wordlist():
        WordVowels = helper(item)
        if WordVowels == vowels:
            List.append(item)
    return List

### DO NOT DELETE THIS LINE: beg testing

print(helper('hello'))


