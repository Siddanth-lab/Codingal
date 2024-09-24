from datetime import date,time,datetime

today=date.today()
now=datetime.now()
print("Today date is", today)
print("Current Date and Time is", now)

print("Date and components", today.year,today.month,today.day)