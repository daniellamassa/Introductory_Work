#Programmer: Dani Massa
import turtle
#this program draws a square
def Square():
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

#this program draws a pentagon
def Pentagon():
    turtle.forward(100)
    turtle.right(72)
    turtle.forward(100)
    turtle.right(72)
    turtle.forward(100)
    turtle.right(72)
    turtle.forward(100)
    turtle.right(72)
    turtle.forward(100)
    turtle.left(108)

#this program draws a star
def Star ():
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)

def NewStar():
    turtle.left(36)
    turtle.forward(100)
    turtle.left(144)
    turtle.forward(100)
    turtle.left(144)
    turtle.forward(100)
    turtle.left(144)
    turtle.forward(100)
    turtle.left(144)
    turtle.forward(100)

#the previous square function that was defined needs to be called
Square()

#this code moves the turtle without drawing on the screen
turtle.penup()
turtle.forward(200)
turtle.pendown()

#the previous pentagon function that was defined needs to be called
Pentagon()

#this code moves the turtle without drawing on the screen
turtle.penup()
turtle.forward(400)
turtle.pendown()
turtle.right(180)

#the previous star function that was defined needs to be called
Star()
