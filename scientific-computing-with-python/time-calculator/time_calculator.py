from datetime import datetime, timedelta

def add_time(start_timestring, duration_timestring, day_of_week=False):

    #get datetimes
    start_datetime = datetime.strptime(start_timestring, "%I:%M %p")
    duration_timedelta = timedelta(hours=int(duration_timestring.split(":")[0]), minutes=int(duration_timestring.split(":")[1]))
    #calculate end datetime
    end_datetime = start_datetime + duration_timedelta
    #get time difference
    day_difference = end_datetime.day - start_datetime.day
    #get end timestring
    end_timestring = end_datetime.strftime("%I:%M %p")
    if(end_timestring[0] == "0"): #remove leading zero fix because of strftime behavior on %I with different systems 
        end_timestring = end_timestring[1:]
    #get day of week of end datetime
    if day_of_week != False:
        day_of_week_int = day_of_week_to_int(day_of_week)
        day_of_week_int += day_difference
        end_day_of_week = int_to_day_of_week(day_of_week_int)
    #get day difference string
    if day_difference == 0:
        day_difference_string = ""
    elif day_difference == 1:
        day_difference_string = " (next day)"
    else:
        day_difference_string = " (" + str(day_difference) + " days later)"
    #generate result string
    if day_of_week != False:
        result = end_timestring + ", " + end_day_of_week + day_difference_string
    else:
        result = end_timestring + day_difference_string
    return result

def day_of_week_to_int(day_of_week):
    day_of_week = day_of_week.lower()
    if day_of_week == "monday":
        return 0
    elif day_of_week == "tuesday":
        return 1
    elif day_of_week == "wednesday":
        return 2
    elif day_of_week == "thursday":
        return 3
    elif day_of_week == "friday":
        return 4
    elif day_of_week == "saturday":
        return 5
    elif day_of_week == "sunday":
        return 6
    else:
        return False
    
def int_to_day_of_week(day_of_week_int):
    if day_of_week_int % 7 == 0:
        return "Monday"
    elif day_of_week_int % 7 == 1:
        return "Tuesday"
    elif day_of_week_int % 7 == 2:
        return "Wednesday"
    elif day_of_week_int % 7 == 3:
        return "Thursday"
    elif day_of_week_int % 7 == 4:
        return "Friday"
    elif day_of_week_int % 7 == 5:
        return "Saturday"
    elif day_of_week_int % 7 == 6:
        return "Sunday"
    else:
        return False