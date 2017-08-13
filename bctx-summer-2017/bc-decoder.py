# Code from Brain Chase Summer 2017 Texas Edition
def main(): 
	ring = {"/":" ", "4":"A", "7":"B", "5":"C", "9":"D", "6":"E"
		, "8":"F", "10":"G", "24":"H", "1":"I", "25":"J"
		, "15":"K", "14":"L", "12":"M", "13":"N", "3":"O"
		, "11":"P", "16":"Q", "17":"R", "23":"S", "26":"T"
		, "21":"U", "19":"V", "18":"W", "20":"X", "22":"Y", "2":"Z"}

	# Need to replace these with real inputs
	#codedMessage = "17 6 4 9 / 26 24 6 / 11 14 4 13 26 23"
	#testMessage = "THE QUICK BROWN"
	codedMessage = input("Please enter your secret message (in numbers): ")
	print()
	print("Here is your decoded message: ")
	decode(codedMessage, ring)
	print()
	

	testMessage = input("Please enter the message you want to encrypt (IN CAPS): ")

	# And potentially call based on a switch to encode or decode
	print()
	print("Here is your scrambled message: ")
	encode(testMessage, ring)
	print()

# Function to decode a message from numbers to letters
# Expects a format of "1 3 5 / 24 2 13"
def decode(msg, ring):
	letters = msg.split(" ")
	
	secretMessage = ""
	for letter in letters:
		if letter in ring:
			secretMessage += ring[letter]	
		else: 
			continue

	print(secretMessage)
	
			
# Function to encode a message from letters to numbers
# Expects a format of "MY MESSAGE"
def encode (msg, ring):
	reverseRing = dict((x,y) for (y,x) in ring.items())
	words = msg.split(" ")	
	encodedMessage = ""
	
	for word in words: 
		for char in word:
			if char in word:
				encodedMessage += reverseRing[char]+" "
			else:
				continue
		encodedMessage += reverseRing[" "]+" "
	
	print(encodedMessage)

main()