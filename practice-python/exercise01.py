# Exercises from http://www.practicepython.org/
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:
# Add on to the previous program by asking the user for another number 
# and printing out that many copies of the previous message. 
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)

from datetime import date

name = input("What is your name?")
print("Nice to meet you, " + name)

age = input("How old are you?")
age = int(age)
futureYear = date.today().year + (100-age)

faveNumber = input("What's your favorite number, " + name + "?")
# Need error handling for non-integer and negatives

for _ in range(int(faveNumber)):
	print("You will turn 100 years old in: " + str(futureYear))
