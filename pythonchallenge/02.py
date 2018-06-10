#!/usr/local/bin/python3
# Code for: Python Challenge 2
# http://www.pythonchallenge.com/pc/def/ocr.html

myFile = open("02.txt", 'r')
lines = myFile.readlines()
myFile.close()

myStr = ''.join(lines)
uniqueChars = set(myStr)

charCount = { uc: myStr.count(uc) for uc in uniqueChars }

rareChars = [ char for char, count in charCount.items() if charCount[char] == 1 ]
rareChars.sort()
print(rareChars)

# Answer: equality
