#Programmer: Dani Massa
import turtle
#this program draws overlapping circles of different colors, which decrease in size by 20 units. 
#I wanted to write a singular function that drew one circle, and then write a program that subtracts 20 from the function
#but I was unsure how to do that, especially with the color change.
turtle.penup()
turtle.goto(0,-300)
turtle.pendown()
turtle.pensize(3)
turtle.speed(10)
turtle.color("black", "firebrick")
turtle.begin_fill()
turtle.circle(300)
turtle.end_fill()
turtle.color("black", "orange red")
turtle.begin_fill()
turtle.circle(280)
turtle.end_fill()
turtle.color("black", "dark orange")
turtle.begin_fill()
turtle.circle(260)
turtle.end_fill()
turtle.color("black", "gold")
turtle.begin_fill()
turtle.circle(240)
turtle.end_fill()
turtle.color("black", "lawn green")
turtle.begin_fill()
turtle.circle(220)
turtle.end_fill()
turtle.color("black", "dark green")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()
turtle.color("black", "dark cyan")
turtle.begin_fill()
turtle.circle(180)
turtle.end_fill()
turtle.color("black", "dodger blue")
turtle.begin_fill()
turtle.circle(160)
turtle.end_fill()
turtle.color("black", "medium blue")
turtle.begin_fill()
turtle.circle(140)
turtle.end_fill()
turtle.color("black", "#4B0082")
turtle.begin_fill()
turtle.circle(120)
turtle.end_fill()
turtle.color("black", "#800080")
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.color("black", "medium violet red")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
turtle.color("black", "deep pink")
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()
turtle.color("black", "hot pink")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()
