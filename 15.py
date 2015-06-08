#!/usr/bin/python3
import datetime
import calendar
for year in range(1586,1996,10):
    if(calendar.isleap(year) and datetime.date(year,1,1).weekday() == 3):
        print(year)
print("Who was born on January 27th 1756?")
print("(Hint: It's Mozart)")
