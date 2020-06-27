####################################################################################################
# Aim:
#This programme gets input from the user on the names of people in their family then they put each person’s name of their family into a spiral 
# Created by : Om Sikaria with the objective of learning Python
####################################################################################################
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green",  "blue",
        "purple","pink", "white", "gray",  "brown" ]
family = []
name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
while name != "":
    family.append(name)
    name = turtle.textinput("My family",
                        "Enter a name, or just hit [ENTER] to end:")
for x in range(100):
    t.pencolor(colors[x%len(family)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(family[x%len(family)], font = ("Arial", int((x+4)/4), "bold") )
    t.left(360/len(family) + 2)
