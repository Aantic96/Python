#Function with 3 arguments, the last one is optional
def add_time(start_time, duration, day = None):

   #Separating starting time into hours, mins and PM or AM
   temp_start_time = start_time.replace(":", " ").split(" ")
   
   #Turning starting hours and mins into integers
   start_hr = int(temp_start_time[0])
   start_min = int(temp_start_time[1])
   
   #Separating time duration into hours and minutes
   temp_duration = duration.split(":")

   hr_dur = int(temp_duration[0])
   min_dur = int(temp_duration[1])

   #Adding the days dictionary for later
   days_dict = {
      1 : "Monday",
      2 : "Tuesday",
      3 : "Wednesday",
      4 : "Thursday",
      5 : "Friday",
      6 : "Saturday",
      7 : "Sunday"
      }

   #Checking whether it is AM or PM
   if temp_start_time[2] == "PM":
      start_hr = start_hr + 12

   #Adding minutes together
   sum_min = start_min + min_dur

   #Definining additional hours that'll be added if minute sum is greater than 60
   additional_hrs = 0
   
   #Loop as long minutes are greater than 60
   while sum_min > 59:
      sum_min = sum_min - 60
      additional_hrs += 1

   #Adding all hours together
   sum_hr = start_hr + hr_dur + additional_hrs

   #Defining day counter
   day_counter = 0

   #Adding to the day counter AND lowering the hours below 24 to fit 24-hr format
   while sum_hr >= 24:
      sum_hr = sum_hr - 24
      day_counter += 1

   #Turns the number from 24-hr format to 12
   if sum_hr >= 13:
      print(str(sum_hr - 12) + ":", end='')
   #Specific case for the midnight hour
   elif sum_hr == 0:
      print(str(12) + ":", end='')
   else:
      print(str(sum_hr) + ":", end='')

   #Adds zero if needed
   if sum_min < 10:
      print("0", end='')

   #Adding mins and checking whether it's AM or PM
   if sum_hr >= 12:
      print(str(sum_min) + " PM", end='')
   else:
      print(str(sum_min) + " AM", end='')
   
   #Triggers if 3rd arg exists
   if day != None:
      #Turns the letters to match those in the dictionary
      day = day.lower().capitalize()

      #Grabs the key and returns it as list
      key = [k for k, v in days_dict.items() if v == day]
      #Turns that list into an int and adds the number of passed days
      key = int(key[0]) + day_counter
      
      #Adjusts key to match the real key in the dictionary
      while key > 7:
         key = key - 7
   
      print(", " + days_dict[key], end='')
   
   #Specific case if only 1 day has passed
   if day_counter == 1:
      print(" (next day)")
   #Any case that is bigger than one day
   elif day_counter > 1:
      print(" (" + str(day_counter) + " days later)")
   #Case if not a full day has passed
   else:
      print("")

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)