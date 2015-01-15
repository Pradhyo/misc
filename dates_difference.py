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


print isafter(2012,12,30,2012,1,1)