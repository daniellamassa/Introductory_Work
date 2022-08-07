#Programmer: Dani Massa
'''
First, I programmed a function that finds the total amount of divisors of a given
number. Then, I applied this function to my MoreDivisors function by calling it within.
I used a series of if and elif statements to compare the number of divisors between two
given numbers. Again, I used elifs instead of an else due to preference.
'''
def Divisors (x):
    counter = 1
    NumDivisors = 0
    while counter <= x:
        if x % counter == 0:
            NumDivisors += 1
        counter += 1
    return NumDivisors

def MoreDivisors (x, y):
    if Divisors (x) > Divisors (y):
        return x
    elif Divisors (y) > Divisors (x):
        return y
    elif Divisors (x) == Divisors (y):
        return x
    
'''
First, I programmed a separate function that makes a list of all the divisors of a given
number. Then I applied this function to GetGCD function from calling it within. Instead of
iterating throught the list from index 0, I decided to iterate backwards because we are trying to
find the GREATEST factor, and the lists are organized in increasing value. I needed to subtract 1 from
each index value (apart from the iteration line of code) because otherwise there would be an IndexError:
list index out of range. Although this program runs, the difference in list length is throwing it off.
My program only compares each index at a time. So for example, with numbers 15 and 20, although they contain a GCF of 5, my program outputs None because the value of 5 for 15 is at index 2, and the value of 5 for 20 is at index 3 (instead of 2 and 2). I am still trying to figure out how to debug this issue.
'''

def ListDivisors(x):
    counter = 2
    Nums = [1]
    while counter <= x:
        if x % counter == 0:
            Nums.append(counter)
        counter += 1
    return Nums
    
def GetGCD (x,y):
    xList = ListDivisors (x)
    yList = ListDivisors (y)
    xindex = len(xList)
    yindex = len(yList)
    while (xindex >= 0) or (yindex >=0):
        valx = xList[(xindex-1)]
        valy = yList[(yindex-1)]
        if valx == valy:
            return valx
        else:
            xindex-= 1
            yindex-= 1
            
'''
After you mentioned that we don't need to use lists to solve this problem, I realized there was a simpler way of solving it. Below is my second attempt, which incorporates the two arguements being divided by each other (depending on which one is larger). However, this still doesn't execute correctly because as the program reassigns variables it becomes flawed. For example, with arguements 15 and 20, as the while loop subtracts 1 from 15 to check for divisors of 20, once it reaches 10 it will return 10 as a divisor, because it has "forgotten" the original value of 15. I think this can be easily fixed by adding a counter variable, however I ran out of time to do so. :(
'''

##def GetGCD (x,y):
##    while (x > y):
##        if x % y == 0:
##            return y
##        elif x % y != 0:
##            y -= 1
##    while (y > x):
##        if y % x == 0:
##            return x
##        elif y % x != 0:
##            x -= 1
##    if x == y:
##        return x


    

