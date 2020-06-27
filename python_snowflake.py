####################################################################################################
# Aim:
#This programme draws a snowflake 
# Created by : Om Sikaria with the objective of learning Python
####################################################################################################
import tkinter as tk
import turtle
root = tk.Tk()
turtle.color("blue")
turtle.shape("turtle")
turtle.pensize(10)
turtle.pencolor("blue")
turtle.speed("fast")
turtle.Screen().bgcolor("red")





def sfv():
    turtle.right(30)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(60)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(30)

def sfa():
    for z in range(0, 4):
        turtle.forward(90)
        sfv()
        turtle.backward(30)
    turtle.backward(240)

def sf():
    for k in range(0, 8):
        sfa()
        turtle.right(45)
sf()
