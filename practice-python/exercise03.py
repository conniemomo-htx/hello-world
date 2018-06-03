#!/usr/bin/emv/python3
# Take a list and print all elements that are less than an upper bound
# Put all those elements in a new list

def main():
	upperBound = input("Enter a number as the upper bound: ")
	# Extra: write this in one line
	# Error handling - test for decimals, alpha characters
		
	numbers = [1,3,4,5,7,8,10]
	newlist = []
	
	for number in numbers:
		if( int(number) < int(upperBound)):
			newlist.append(number)
	
	print(newlist)
			
main()			
