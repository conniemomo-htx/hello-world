import re

def is_isogram(string):
    testStr = string

    # Strip out all non-word
    rec = re.compile('[a-zA-z]{1}')
    alphaOnly = ''.join(rec.findall(testStr))

    # When just letters, convert to lowercase
    alphaOnly = alphaOnly.lower()

    # With just lowercase letters test for repeated characters
    unique = set(alphaOnly)
    orig = list(alphaOnly)

    isIso = False
    if ( len(unique) == len(orig) ):
        isIso = True

    return isIso

if __name__ == '__main__':
    is_isogram(input("Enter Text to Test: "))
