def verify(isbn):
    returnVal = False
    checkVal = 0

    chars = []
    ISBN10 = [10,9,8,7,6,5,4,3,2,1]
    ISBN13 = [13,12,11] + ISBN10

    # Strip hyphens
    origIsbn = isbn
    isbn = ''.join(isbn.split('-'))

    try:

        if (len(isbn) < 10):
            raise ValueError("ISBN is too short: " + origIsbn)
        elif (len(isbn) > 10):
            raise ValueError("ISBN is too long: " + origIsbn)
        else:
            # 10 characteres, and each character needs to be digit or X
            for i in range(0, len(isbn)):
                if (isbn[i].isdigit()):
                    chars += isbn[i]
                    checkVal += int(isbn[i]) * ISBN10[i]
                    print(int(isbn[i]) * ISBN10[i])
                elif (isbn[i]=="X"):
                    # X can only be in last position
                    if (i != len(isbn)-1):
                        raise ValueError("X can only be in the last position. Current position: ", i)
                    else:
                        checkVal += 10
                else:
                    raise ValueError("ISBN contains an invalid character: " + isbn[i])

            isbn = "".join(chars)

            if (checkVal % 11 == 0):
                returnVal = True
            else:
                raise ValueError("Invalid ISBN: ", checkVal % 11)

    except ValueError as err:
        print("ERROR: ", err.args)

    print(isbn)
    print(checkVal % 11)

    return returnVal

if __name__ == '__main__':
    verify(input("Enter ISBN: "))
