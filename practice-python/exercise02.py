#Ask the user for a number. Depending on whether the number 
#is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when 
#divided by 2?
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) 
#and one number to divide by (check). If check divides evenly 
#into num, tell that to the user. If not, print a different appropriate message.

def main():
	num = input("Please enter a number: ")
	msg = "Your number is "

	# Need to check for decimals and round
	# Need to check for alphabet and symbols 
			
	if (int(num) == 0):
		msg += "zero. "
		
	elif (int(num) % 2 == 0):
		msg += "even. "
		
		if(int(num) % 4 == 0):
			msg += "It is also a multiple of 4."	
			
	else:
		msg += "odd. "
		
	print(msg)

main()
