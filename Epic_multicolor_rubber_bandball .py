####################################################################################################
# Aim:
#This programme draws a rubber band ball in multiple colours multiple times
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
sides = 6
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.Screen().bgcolor("black")
for x in range (0,1250):
    turtle.pencolor(colors[ x % sides ])
    turtle.forward(x * 3 / sides + x)
    turtle.left(360 / sides + 1)
    turtle.width(x*sides/100)
    turtle.left(90)
