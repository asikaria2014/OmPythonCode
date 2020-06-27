####################################################################################################
# Aim:
#This programme draws a rosette based on the input given by the user
#
#
#
#
# Created by : Om Sikaria with the the objective of learning Python
####################################################################################################
import turtle
turtle.color("blue")
turtle.shape("turtle")
turtle.speed(0)
turtle.width (3)
turtle.Screen().bgcolor("black")
noOfCircles = int(turtle.numinput("number of circles","how many circles do you wantas part of your rosette"))
for x in range (noOfCircles):
    turtle.pencolor('red')
    turtle.circle(300)
    turtle.pencolor('orange')
    turtle.circle(250)
    turtle.pencolor('yellow')
    turtle.circle(200)
    turtle.pencolor('green')
    turtle.circle(150)
    turtle.pencolor('blue')
    turtle.circle(100)
    turtle.left(360 /noOfCircles )
