import datetime

born_date = int (input ('Введіть дату Вашого народження: '))
time_now = datetime.datetime.utcnow()
current_year = time_now.year
age = current_year - born_date

print ('Ваш вік:' , age )



