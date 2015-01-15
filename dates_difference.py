# Program to find difference between two dates

def nextDay(year, month, day):
    """Returns date of next day"""
    day += 1
    if day == daysinmonth(month,year)+1:
        day = 1
        month += 1
    if month == 13:
        month = 1
        year += 1
    
    return year, month, day

def daysinmonth(month,year):
	"""Returns number of days in month"""
	dayspermonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if isleap(year):
		dayspermonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return dayspermonth[month-1]

def isleap(year):
	"""Returns true if leap year"""
	if year%400==0:
		return True
	elif year%100==0:
		return False
	else:
		return year % 4==0

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
    #assert isafter(year1, month1, day1, year2, month2, day2)       
    days = 0
    while isafter(year1, month1, day1, year2, month2, day2):
        days+=1
        year1,month1,day1 = nextDay(year1, month1, day1)
        
    return days



print daysBetweenDates(1992,6,9,2015,1,15)
print daysBetweenDates(1915,1,15,2015,1,15)
print daysBetweenDates(1992,1,1,1991,12,20)
print daysBetweenDates(1900, 1, 1, 1999, 12, 31)