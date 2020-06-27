####################################################################################################
# Aim:
#This program is an english dictionary. Ask for the meaning of any word and you should have the resonse.
#
#
# Note: This connects to an open MySQL Database with the meaning of the words.
# I am aware that the code contains the connection details, however this is
# publicly available and there are no licensing implications.
#
#
#
# Created by : Om Sikaria with the the objective of learning Python
####################################################################################################



import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")
