# Programmer: Dani Massa

# This function takes two given lists, and returns a new list that contains
# those values from the first list that are not contained in the second list. 
def difference(alist, blist):
    NewList = []
    for item in alist:
        if item not in blist:
            NewList.append(item)
    return NewList


### DO NOT DELETE THIS LINE: beg testing

alist = [3, 1, 6]
blist = []
print("List", alist, "without list", blist, "is:", difference(alist, blist))

alist = [3, 5, 8, 6, 4, 2]
blist = [1, 5, 9, 56]
print("List", alist, "without list", blist, "is:", difference(alist, blist))


alist = [3,4,3,3,5,6,4]
blist = [3, 6, 9]
print("List", alist, "without list", blist, "is:", difference(alist, blist))

