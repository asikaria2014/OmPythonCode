
####################################################################################################
# Aim:
#This program is an english dictionary. Ask for the meaning of any word and you should have the resonse.
#
#
#
# Created by : Om Sikaria with the the objective of learning Python
####################################################################################################


import json                                                               # imports json module
from difflib import get_close_matches                                     # imports get_close_matches from difflib module

data = json.load(open("data.json"))                                       # opens data.json this is where the key value pairs of ["word" : "Definition"] is

def translate(w):                                                         # defines function
    w = w.lower()                                                         # turns user input into lower case
    if w in data:                                                         # checks if the word that the user entered is in data.json
        return data[w]                                                    # returns the definition of the word
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":                                                     # checks if yn is Y
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":                                                   # checks if yn is N
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter a word and I will return its definition for you: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
