#!/usr/bin/python3
import datetime
import calendar
out = [year for year in range(1586,1996,10) 
       if(calendar.isleap(year) and datetime.date(year,1,1).weekday() == 3)]
print("Who was born on January 27th {0[0]}?".format(out))
print("(Hint: It's Mozart)")
