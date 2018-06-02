#!/usr/local/bin/python3
# Code for: Python Challenge 2
# http://www.pythonchallenge.com/pc/def/map.html

def decode(y, alpha):
    returnVal = y

    if (y in alphabet):
        if (y == "y"):
            returnVal = alphabet[0]
        elif (y == "z"):
            returnVal = alphabet[1]
        else:
            returnVal = alphabet[ alphabet.index( y ) + 2 ]

    return returnVal

# Main Program
msgTxt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. "
msgTxt += "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. "
msgTxt += "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# Debug/Answer case
# msgTxt = "map"

# Original solution
alphabet = list("abcdefghijklmnopqrstuvwxyz")
decodedMessage = ''.join([decode(x, alphabet) for x in list(msgTxt)])

# with maketrans
key = "cdefghijklmnopqrstuvwxyzab"
decodedMessage = msgTxt.translate(msgTxt.maketrans(''.join(alphabet), key))

print(decodedMessage)

''' ANSWER
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and tha
t's why this text is so long. using string.maketrans() is recommended. now apply on the url.
'''
