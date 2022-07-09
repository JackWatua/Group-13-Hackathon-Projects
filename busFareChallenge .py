#CHALLANGE 1 DAY 1  - BUS FARE CHALLANGE

#accepts one arguement date
def determine_fare(date):
  print("Today\'s bus fare Checker".center(60, " "))
  print("-"  * 60, "\n")
  #create a  tuple of all weekdays
  week_days = ('Mon','Tue','Wed','Thur','Fri','Sat','Sun')
  #get weekday from date
  day = week_days[date.weekday()]
  #if day is saturday or sunday...
  if day in week_days[5:]:
    #if day is saturday (week_days[5]) 
    if day == week_days[5]:
      fare = 60 #set fare to 60
    else:
      #if day is sunday(week_days[6])
      fare = 80  #set fare to 80
  #if bay is between mon - fri 
  else:
    fare = 100 #set fare to 80

  print(f"Date : {date}") #print date
  print(f"Day : {day}") # print weekday
  print(f"Fare : {fare}") #print fare
  print("-"  * 60, "\n\n") #underline using _ 


