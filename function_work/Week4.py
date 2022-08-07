#1.
def smaller (x,y):
    if x>=y:
        return y
    else:
        return x

#2.
def smaller3 (x,y,z):
    if x<=y and x<=z:
        return x
    elif y<=x and y<=z:
        return y
    elif z<=x and z<=y:
        return z
    elif x==y==z:
        return x

#3.
def smaller4 (x,y,z):
    smaller (x,y)
    if x<= y and x<=z:
        return x
    if y<=x and y<=z:
        return y
    elif z<=x and z<=y:
        return z
    elif x==y==z:
        return x

#4.
def counter (x):
    totalsum = 0
    while x >= 1:
        totalsum = totalsum + x
        x = x-1
    return totalsum

#5.
def squaredcounter (x):
    squaredsum = 0
    while x >= 1:
        squaredsum = squaredsum + (x**2)
        x = (x-1)
    return squaredsum

#6.
def fib (x):
    firstfib = 0
    secondfib = 1
    x = x -2
    while x >= 1:
        nextfib = firstfib + secondfib
    print(firstfib, secondfib, )
