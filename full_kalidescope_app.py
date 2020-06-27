####################################################################################################
# Aim:
#This programme lets the user build their own kaleidoscope when they have full control on everything that's going on 
#
# Created by : Om Sikaria with the the objective of learning Python
####################################################################################################
import random
import turtle
import sys
#from tkinter import*
#w=Tk()
#w.title("turtle width")

t = turtle.Pen()
t.speed(0)
t.shape("turtle")
turtle.bgcolor('black')
t.pencolor("white")
t.width(0)
width = t.width()



def draw_In_Kaleido(x,y):
    sp_sh = turtle.textinput("spirals or shapes","Do you want to draw a spiral or a shape? type sp for spiral and type sh for a shape")
    sp_sh = sp_sh.lower()



    if sp_sh == "sh":
        shape_size = int(turtle.numinput("size of shape","how big do you want your shape to be 10 - 100",  50, 10, 100))
        whatshape = int(turtle.numinput("sides of shape","how many sides do you want your shape to have 3 to 10. For a Circle enter 11 ",  4, 3, 11))
        angle = t.heading()
        t.penup()
        t.setpos(x,y)
        t.pendown()

        # If 11 entered then this code draws a circle
        if whatshape == 11:
            t.penup()
            t.setpos(x,y)
            t.pendown()
            t.setheading(180-angle)
            t.circle(shape_size/2)

            t.penup()
            t.setpos(-x,y)
            t.pendown()
            t.setheading(180-angle)
            t.circle(shape_size/2)

            t.penup()
            t.setpos(-x,-y)
            t.pendown()
            t.setheading(180-angle)
            t.circle(shape_size/2)

            t.penup()
            t.setpos(x,-y)
            t.pendown()
            t.setheading(180-angle)
            t.circle(shape_size/2)

        # For all other shapes (apart from Circle) based on the sze and number of sides selected
        else:
            for l in range(whatshape):
                t.forward(shape_size)
                t.left(360/whatshape)
            t.penup()
            t.setpos(-x,y)
            t.pendown()
            t.setheading(180-angle)

            for l in range(whatshape):
                t.forward(shape_size)
                t.right(360/whatshape)
            t.penup()
            t.setpos(-x,-y)
            t.pendown()
            t.setheading(angle-180)

            for l in range(whatshape):
                t.forward(shape_size)
                t.left(360/whatshape)
            t.penup()
            t.setpos(x,-y)
            t.pendown()
            t.setheading(360-angle)

            for l in range(whatshape):
                t.forward(shape_size)
                t.right(360/whatshape)

        user_inputs()

    # Draws a spiral based on the answers to the questions
    if sp_sh == "sp":
        sides = int(turtle.numinput("sides on spiral","how many sides do you want on your spiral 2 - 10",  4, 2, 10))
        size = int(turtle.numinput("size of spiral","how big do you want your spiral to be 10 - 40",  25, 10, 40))
        angle = t.heading()
        t.penup()
        t.setpos(x,y)
        t.pendown()

        for m in range(size):
            t.forward(m*2)
            t.left(360/sides + 2)
        t.penup()
        t.setpos(-x,y)
        t.pendown()
        t.setheading(180-angle)

        for m in range(size):
            t.forward(m*2)
            t.right(360/sides + 2)
        t.penup()
        t.setpos(-x,-y)
        t.pendown()
        t.setheading(angle-180)

        for m in range(size):
            t.forward(m*2)
            t.left(360/sides + 2)
        t.penup()
        t.setpos(x,-y)
        t.pendown()
        t.setheading(360-angle)

        for m in range(size):
            t.forward(m*2)
            t.right(360/sides + 2)

        user_inputs()


def redpen():
    t.pencolor("red")
def orangepen():
    t.pencolor("orange")
def yellowpen():
    t.pencolor("yellow")
def greenpen():
    t.pencolor("green")
def bluepen():
    t.pencolor("blue")
def purplepen():
    t.pencolor("purple")
def violetpen():
    t.pencolor("violet")
def widen():
    t.width(t.width() + 2)
def thinen():
    t.width(t.width() - 2)

# user_input function allows users to make some choices
#   w - widen the thinkness of the lines he wants to draw
#   t - make the lines thinner
#   User can change colours of the turle
#               r = Red
#               y = Yellow
#               o = Orange
#               g = green
#               b = blue
#               p = purple
#               v = violet
def user_inputs():
    turtle.listen()
    turtle.onkeypress(widen, "w")
    turtle.onkeypress(thinen, "t")
    turtle.onkeypress(redpen, "r")
    turtle.onkeypress(orangepen, "o")
    turtle.onkeypress(yellowpen, "y")
    turtle.onkeypress(greenpen, "g")
    turtle.onkeypress(bluepen, "b")
    turtle.onkeypress(purplepen, "p")
    turtle.onkeypress(violetpen, "v")


user_inputs()
turtle.onscreenclick(draw_In_Kaleido)
