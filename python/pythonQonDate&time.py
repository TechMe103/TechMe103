#Exercise 1: Print current date and time in Python
import datetime

print(datetime.datetime.now())

print(datetime.datetime.now().time())#only time


#sol2 using strftime()
from time import gmtime, strftime

print(strftime("%Y-%m-%d  %H:%M:%S"  , gmtime()))

#Exercise 2: Convert string into a datetime object
from datetime import datetime

date_string="Mar 1 2007  4:20PM"
datetime_object=datetime.strptime(date_string , '%b %d %Y %I:%M%p')
print(datetime_object)


#Exercise 3: Subtract a week (7 days)  from a given date in Python
from datetime import datetime, timedelta

given_date=datetime(2020 , 2, 25)
print("Given date")
print(given_date)

days_to_substract= 7
res_date=given_date - timedelta(days=days_to_substract)
print("New Date")
print(res_date)

#Exercise 4: Print a date in a the following format
from datetime import datetime

given_date=datetime(2024 , 1, 3)
print("Given date is:") 
print(given_date.strftime('%A %d %B %Y'))


#Exercise 5: Find the day of the week of a given date
from datetime import datetime

given_date=datetime(2020 , 7 , 23)
print(given_date.today().weekday())

print(given_date.strftime('%A'))

#sol 2 using calender module
import calendar
from datetime import datetime

given_date=datetime(2020 , 7, 24)
weekday=calendar.day_name[given_date.weekday()]
print(weekday)

#Exercise 6: Add a week (7 days) and 12 hours to a given date
from datetime import datetime , timedelta

given_date=datetime(2020 , 3, 22, 10, 00, 00)
print("given date")
print(given_date)

days_to_add=7
res_date=given_date + timedelta(days=days_to_add , hours=12)
print("New Date")
print(res_date)

#Exercise 7: Print current time in milliseconds
import time

milliseconds= int(round(time.time() * 1000))
print(milliseconds)

#Exercise 8: Convert the following datetime into a string
from datetime import datetime

given_date=datetime(2020 , 2, 25)
string_date= given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)

#Exercise 9: Calculate the date 4 months from the current date
from datetime import datetime
from dateutil.relativedelta import relativedelta

#2020-02-25
given_date= datetime(2020 , 2, 25).date()

months_to_add = 4
new_date = given_date + relativedelta(months=+ months_to_add)
print(new_date)

#Exercise 10: Calculate number of days between two given dates
from datetime import datetime

date_1= datetime(2020 , 2, 25).date()
date_2=datetime(2020 , 9 , 17).date()

delta=None
if date_1 > date_2:
    print("date_1 is greater")
    delta= date_1 - date_2
else:
    print("date_2 is greater")
    delta= date_2 - date_1
print("Difference is" , delta.days , "days")


