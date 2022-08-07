def SumAll(list1):
    index = 0
    total = 0
    while (index<len(list1)):
           val = list1[index]
           total = total + val
           index += 1
    return total

def SumGreater10(list1):
    index = 0
    total = 0
    while (index<len(list1)):
           val = list1[index]
           if val >= 10:
               total = total + val
           index += 1
    return total

def SumGreaterN (list1, N):
    index = 0
    total = 0
    while (index<len(list1)):
        val = list1[index]
        if val >= N:
            total = total + val
        index += 1
    return total

def SumDivisors (list1, D):
    index = 0
    total = 0
    while (index<len(list1)):
        val = list1[index]
        if val %D == 0:
            total = total + val
        index += 1
    return total 
