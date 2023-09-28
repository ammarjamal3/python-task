import datetime
from datetime import timedelta

def getdate():

   date_components1 = input('Enter a date formatted as YYYY-MM-DD: ').split('-')
   print(date_components1)
   
   date_components2 = input('Enter a date formatted as YYYY-MM-DD: ').split('-')
   print(date_components2)

   year, month, day = [int(item) for item in date_components1]
   year2, month2, day2 = [int(item) for item in date_components2]
   
   time_of_date1=((year*360*24)+(month*30*24)+(day*24))
   time_of_date2=((year2*360*24)+(month2*30*24)+(day2*24))

   if time_of_date1 > time_of_date2:
      result= time_of_date1 - time_of_date2
   else: result= time_of_date2 - time_of_date1
   print(result,'hours')

getdate()
