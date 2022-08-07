# Programmers: Dani and Lucas

l1 = [1,2,3,4,5]
def NumOdd (l1):
    index = 0
    odd = 0
    while (index < len(l1)):
        val = l1[index]
        if val % 2 == 1:
            odd += 1
        index += 1
    return(odd)
print(NumOdd(l1))

l2 = [1,2,3,4,5]
def GreaterThan(l2, a):
    index = 0
    numCount = 0
    while (index<len(l2)):
        val = l2[index]
        if val > a:
            numCount +=1
        index += 1
    return numCount
print(GreaterThan(l2, 3))

l3 = [10,20,30]
def GetIndex (l3, b):
    index = 0
    while (index < len(l3)):
        if index == len(l3)-1:
            return -1
        elif b != l3[index]:
            index += 1
        elif b == l3[index]:
            return index
    return index
print(GetIndex(l3,17))

l4 = [3,1,4,1,5,9]
def GetLastIndex (l4, b):
    index = len(l4)-1
    while (index >= 0):
        if b != l4[index]:
            index -= 1
        elif b == l4[index]:
            return index
        elif index == 0:
            index = -1
    return index
print(GetLastIndex(l4,1))
