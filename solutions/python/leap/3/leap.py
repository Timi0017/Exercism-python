"Module to check whether a number is a leap year"
def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        
