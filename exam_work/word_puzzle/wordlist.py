
def get_wordlist ():
    """This function reads a list of words from a file called
    wordlist.txt and returns those words as a Python list of
    strings. It converts all letters to lower case letters."""

    datafile = open("wordlist.txt", 'r')

    wordlist = []

    for line in datafile:
        line = line.strip()
        wordlist.append(line.lower())

    return wordlist
