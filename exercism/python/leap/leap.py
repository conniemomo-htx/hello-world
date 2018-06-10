def is_leap_year(year):
    isLY = False
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                isLY = True
            else:
                isLY = False
        else:
            isLY = True
    else:
        isLY = False

    return isLY
