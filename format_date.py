#To get the current date and time We need to use the date time library
from datetime import datetime

#The now function returns current date and time
today = datetime.now()

# use day, month, year, minute, second functions
# to display only part of the date
# All these functions return integers
# Convert them to strings before concatenating them in to another string
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))