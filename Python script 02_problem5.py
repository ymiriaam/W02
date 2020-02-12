# Prompting user to enter a year
year = int(input("Enter Year"))

# Verifying that it is a valid year
try:
    valid_year = '%year'
except ValueError:
    print('invalid year!')

# Checking if year is a leap year
if year % 4 == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print ("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print ("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
