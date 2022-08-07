#Programmer: Dani Massa

# Need to import math to use the math.sqrt function in def Overlaps
import math

# This function finds the area of a rectangle given its width and height by
# multiplying the two values together.
def RectArea (w,h):
    A = w*h
    return A

'''
This function tells you if a rectangle is a square, or if its width or height
is larger by comapring these two values. Although I could've used an if-elif-else 
sequence, I chose to write two elif statements because I find it easier to
understand and it is more user-readable.
'''

def Shape (w,h):
    if w > h:
        return ("wide")
    elif h > w:
        return ("tall")
    elif w == h:
        return ("square")
'''
This functions returns a boolean value dependent on whether two rectangles overlap.
I defined the distance formula as a variable to find the distance between the two
upper-right hand corners of the boxes. If this numerical distance value exceeds
the sum of the heights and widths of the two boxes, they do not overlap. However
if the distance value is less than (or equal to) BOTH the sum of the heights and
widths, there will be overlap.
'''

def Overlaps (x1, y1, w1, h1, x2, y2, w2, h2):
    D = math.sqrt ((x2-x1)**2 + (y2-y1)**2)
    if D > (w1 + w2) and D > (h1 + h2):
        return False
    else:
        return True
