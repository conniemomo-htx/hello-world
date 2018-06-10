def is_isogram(string):
    testStr = string

    # Strip out all non-word, and set to lowercase
    alphaOnly = ''.join( [ c.lower() for c in testStr if c.isalpha()] )

    # Compare the length of the set (unique) vs original string length
    return ( len(  set(alphaOnly) ) == len(  list(alphaOnly) ) )

if __name__ == '__main__':
    is_isogram(input("Enter Text to Test: "))
