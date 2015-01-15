# Program to find difference between two dates

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def isafter(year1, month1, day1, year2, month2, day2):
    """Returns True if date2 is after date1"""
    if (year2-year1)*1000+(month2-month1)*50+(day2-day1)<=0:
        return False
    return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    days = 0
    while isafter(year1, month1, day1, year2, month2, day2):
        days+=1
        year1,month1,day1 = nextDay(year1, month1, day1)
        
    return days



print daysBetweenDates(1992,6,9,2015,1,15)