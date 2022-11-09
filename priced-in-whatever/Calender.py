
import datetime

def cleanDate(date):
    newDate = datetime.datetime.strptime(date, "%Y-%m-%d")
    return newDate.strftime("%d/%m/%Y")

def getYear(date):
    return int(date[6:])

def getMonth(date):
    return int(date[3:5])

def getDay(date):
    return int(date[:2])

def compare(date1, date2): # return 1 if date 1 is after date2
    year1 = getYear(date1)
    year2 = getYear(date2)
    month1 = getMonth(date1)
    month2 = getMonth(date2)
    day1 = getDay(date1)
    day2 = getDay(date2)
    if year1 > year2:
        return 1
    elif year1 < year2:
        return -1
    elif year1 == year2:
        if month1 > month2:
            return 1
        elif month1 < month2:
            return -1
        elif month1 == month2:
            if day1 > day2:
                return 1
            elif day1 < day2:
                return -1
            elif day1 == day2:
                return 0
