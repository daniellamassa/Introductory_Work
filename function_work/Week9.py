#Programmer: Dani Massa

# This function uses a takes a given number between 1-12, and returns
# a string containing the name of the corresponding month.

def NumToMonth(number):
    Dict = {1:'January', 2:'Feburary', 3:'March', 4:'April',
            5:'May', 6:'June', 7:'July', 8:'August',
            9:'September', 10:'October', 11:'November', 12:'December'}
    for num in Dict:
        if (number == num in Dict):
            month = Dict[number]
            return month

# This function takes a given number and index, and returns the
# nth place of that number.

def GetNthPlace(number, index):
    Divider = 10**index
    NewNumber = number//Divider
    if (index == 0):
        ReturnValue = NewNumber%(Divider*10)
    else:
        ReturnValue = NewNumber%(Divider)
    return (ReturnValue)

# This function does the same as the GetNthPlace function, but instead
# uses strings. I believe that this is better because strings allows for
# slicing to be used, which overall makes the function easier to write and also
# improves readability.

def GetNthPlaceString(number, index):
    StringNumber = str(number)
    if index > len(StringNumber):
        return ('0')
    elif (index == 0):
        NewString = StringNumber[index+2:]
        return int(NewString)
    else:
        NewString = StringNumber[len(StringNumber)-index:]
        return int(NewString)
