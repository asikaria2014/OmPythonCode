####################################################################################################
# Aim:
#In this programme a computer randomly generates A number between one and 20 and you need to guess that number within five chances
# Created by : Om Sikaria with the objective of learning Python
####################################################################################################
import random
choice = int(random.randint(1,20))
score=5
guesses=1
question= int(input('''Enter a number between 1 and 20. You have 5 chances to guess the number. Best of Luck !  \n'''))
while choice!=question and guesses < 5:
    if question > choice:
         print("too big")
         guesses+=1
         score -=1
         question= int(input("Enter a number between 1 and 20. \n"))
    elif question < choice:
        print("too small")
        guesses+=1
        score -= 1
        question = int(input("Enter a number between 1 and 20. \n"))
    if guesses == 5 and choice != question:
        print("You lose as you took too many guesses")
        print("your score was 0")
    if choice == question and guesses == 1:
        print("You Win")
        print ("you took 1 guess and your score was 5 out of 5 - COOOL !!! ")
    if choice == question and guesses == 2:
        print("You Win")
        print ("you took 2 guesses and your score was 4 out of 5")
    if choice == question and guesses == 3:
        print("You Win")
        print ("you took 3 guesses and your score was 3 out of 5")
    if choice == question and guesses == 4:
        print("You Win")
        print ("you took 4 guesses and your score was 2 out of 5")
    if choice == question and guesses == 5:
        print("You Win")
        print ("you took 5 guesses and your score was 1 out of 5")
