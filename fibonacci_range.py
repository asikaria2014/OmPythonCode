####################################################################################################
# Aim:
#This program generates the Fibonacci series from begining till the number you specify. Enjoy !
#Learn more about what is the fasinating series this is here - https://en.wikipedia.org/wiki/Fibonacci_number
#
# Created by : Om Sikaria with the the objective of learning Python
####################################################################################################


## This takes input from the user
upto = int(input("enter a number and I will show numbers of fibonacci series upto that number "))

a = 0
b = 1
c = 1

if (upto>0):
    print(0)

    for i in range(1, upto):
        print(c)
        c = a + b
        a = b
        b = c
        if (c >= upto):
            break
else:
    print("Positive numbers only please")
