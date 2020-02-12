# Determining whether the year is a leap year or not
# A year is a leap year if it is divisible by 4, but not by 100 unless it is divisible by 400.

year = 2000

if (year % 4 == 0):                             # If it is divisible by 4
    if (year % 100) == 0:                       # If it is divisible by 100
        if (year % 400) == 0:                   # If it is divisible by 400
            print ("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print ("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
