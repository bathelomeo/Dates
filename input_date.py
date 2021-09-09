from datetime import datetime,timedelta

birthday = input('When is your birthday (dd/mm/yyyy)?')

birthday_date = datetime.strpftime(birthday, '%d/%m/%Y')

print('birthday:' + str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))