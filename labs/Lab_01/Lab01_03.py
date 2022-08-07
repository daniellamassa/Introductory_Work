#Programmer: Dani Massa
import turtle
#this program adjusts the turtle's visability and start position
#I considered using .goto but found directionals to be better than coordinates 
turtle.hideturtle()
turtle.penup()
turtle.backward(200)
turtle.pendown()
turtle.showturtle()

#this program draws the first circle
turtle.pensize(10)
turtle.pencolor("blue")
turtle.circle(80)

#this program moves the turtle without drawing
turtle.penup()
turtle.forward(190)
turtle.pendown()

#this program draws the second circle
turtle.pencolor("black")
turtle.circle(80)

#this program moves the turtle without drawing
turtle.penup()
turtle.forward(190)
turtle.pendown()

#this program draws the third circle
turtle.pencolor("red")
turtle.circle(80)

#this program moves the turtle to the correct position for the green circle
#to find the proper coordinates I used print(turtle.position()) and then removed it
#this program also flips the direction the turtle is facing
turtle.right(180)
turtle.penup()
turtle.goto(85,75)
turtle.pendown()

#this program draws the fourth circle
turtle.pencolor("green")
turtle.circle(80)

#this program moves the turtle without drawing
turtle.penup()
turtle.forward(190)
turtle.pendown()

#this program draws the fifth circle
turtle.pencolor("yellow")
turtle.circle(80)

#I considered using functions in this assignment because there is repetition in the code, but
#I decided that it was best not to use them 


