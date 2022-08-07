#Programmer: Dani Massa

import random

def Lottery():
    length = 0
    List = []
    while (length < 7):
        List.append(random.randint(0,9))
        length += 1
    return List

def LargerThan(List, number):
    NewList = []
    index = 0
    while (index < len(List)):
        if (List[index] > number):
            NewList.append(List[index])
        index += 1
    return NewList

def SmallerThanCount(List, number):
    index = 0
    count = 0
    while (index < len(List)):
        if (List[index] < number):
            count += 1
        index += 1
    return count

def Lowest (List):
    smallest = List[0]
    for num in List:
        if (num < smallest):
            smallest = num
    return smallest

def DropLowest(List):
    lowest = Lowest(List)
    List.remove(lowest)
    return List

def CountDigits(String):
    counter = 0
    for unit in String:
        if (unit.isdigit() == True):
            counter += 1
    return counter

def CapTee(String):
    NewString = ""
    for item in String:
        if (item == 't'):
            NewString = NewString + 'T'
        else:
            NewString = NewString + item
    return NewString

def DigitSum(String):
    total = 0
    numbers = ('1','2','3','4','5','6','7','8','9','0')
    for item in String:
        if item in numbers:
            item = int(item)
            total = total + item
    return total
