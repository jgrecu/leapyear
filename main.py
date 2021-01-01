# take input a year and print out if the year is leap year (True) or not (False)
def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        return True
    return False


print(is_leap(int(input("Enter year: "))))
