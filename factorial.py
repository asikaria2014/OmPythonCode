####################################################################################################
# Aim:
#This code finds the factorial of a given number that the user enters#
#
#
#
# Created by : Om Sikaria with the the objective of learning Python
####################################################################################################

## This takes input from the user
fac = int(input("Enter the number that you want the factorial of: "))

## This for loop calculates the factorial. Iterates in reverse order
## although you can iterate in the normal order as well if you like (with a little bit of changes)
for i in range(fac,2,-1):
    fac = fac*(i-1)

## Hows the output to the user
print(" The factorial is : " + str(fac))
