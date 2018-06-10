import string

def is_pangram(sentence):
    alphabet = string.ascii_lowercase

    # Strip out all non-word, and set to lowercase
    alphaOnly = [ c.lower() for c in sentence if c.isalpha() ]

    # Compare the length of the set (unique) vs original string length
    return ( len( alphabet ) == len(  set(alphaOnly) ) )

if __name__ == '__main__':
    is_pangram(input("Enter Sentence to Test: "))
