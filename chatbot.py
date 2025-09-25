#Program: Chatbot
#Name: Shenghua Jin
#Date: 9/17/2025

import random

greeting = "Hello! I am a chatbot created by Simon Jin"
print(greeting)
#Ask a question and use input without assigning a variable to name
print("Your name is:" + str(input("Hello, what's your name?")))
age = input("What's your age?")
country = input("Where do you live?")
try:    
    if int(age) > 18 :
        if country.strip().upper() == "CHINA":
            print("You have a firewall.")
    if int(age) < 18:
        print(f"You are a minor and {age} years old. Do not use this program")
        print(True)
except ValueError:
    print("That is not a valid age")
major = input("What is your major?")

#While loop to create a list of favorite foods
print("What are your favorite foods? input . to stop")
favFoods = []
for x in range(0,3):
    if(input() == "."):
        break
    else:
        favFoods.append(input())

#Pick a food at random and use it in the output
print("My favorite food is also: " + random.choice(favFoods))

#If/else to give an output
if len(favFoods) <= 2:
    print("You don't have alot of favorite foods")
else:
    print("You have alot of favorite foods")

# Ask for favorite book and compare to a library that we have. Give output accordingly
library = ["The Great Gatsby", "Paradise Lost", "Harry Potter", "Dante's Inferno", "Don Quixote"]
yourBook = input("What is your favorite book?").strip()
print("Our library has the books:")
#For loop to display the library
for x in library:
    print(x)
#Series of conditionals. 2 elif statements
if len(yourBook) < 5 and age == 25:
    print("That book name is too short, we don't have it in our library.")
elif len(yourBook) > 25 or age == 80:
    print("That book name is too long or you are too old, we don't have it in our library.")
elif yourBook[0] == "A":
    print("Your book starts with the letter A. I hate that letter")
else:
    #Go through library to see if it is in the library. Upper make it not case sensitive
        if yourBook in library:
            print("We have that book in our library!")
        else:
            print("It seems that book isn't in our library.")











