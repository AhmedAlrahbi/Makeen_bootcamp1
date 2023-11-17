#PS_in-class-activity, earliest time calc
time = input("Enter time in this format (00:00)-(12:00)? ")
dayTime = input("AM or PM? ")
time1 = input("Enter time in this format (00:00)-(12:00)? ")
dayTime1 = input("AM or PM? ")
if dayTime.upper() == "AM" and dayTime1.upper() == "PM":
    print(time, dayTime, " and then", time1, dayTime1 )
elif dayTime.upper() == "PM" and dayTime1.upper() == "AM":
    print(time1, dayTime1, " and then", time, dayTime )
else:
    if str(time).replace(":", "") > str(time1).replace(":", ""):
        print(time1, dayTime1, " and then" ,time, dayTime )
    elif str(time).replace(":", "") < str(time1).replace(":", ""):
        print(time, dayTime, " and then " ,time1, dayTime1 )
    else:
        print("Its the same time")