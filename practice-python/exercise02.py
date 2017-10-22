#Ask the user for a number. Depending on whether the number 
#is even or odd, print out an appropriate message to the user. 
#Hint: how does an even / odd number react differently when 
#divided by 2?
#Extras:
#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) 
#and one number to divide by (check). If check divides evenly 
#into num, tell that to the user. If not, print a different appropriate message.

def checkDivisible(num, div):
	msg = "Your number is "
	
	# Need to check for decimals and round
	# Need to check for alphabet and symbols 
	
	if (int(num) == 0):
			msg += "zero. "
				
	elif (int(num) % int(div) == 0):
		msg += num + " and is divisible by " + div + ". "	

	else:
		msg += num + " and is not divisible by " + div + ". "
	
	return msg		
			

def main():
	num = input("Please enter a number: ")
	div = input("Check to see if it is divisible by: ")
		
	msg = checkDivisible(num, div)	
	print (msg)
		
	if (int(num) % 4 == 0):
		print("It is also a multiple of 4.")	

main()
