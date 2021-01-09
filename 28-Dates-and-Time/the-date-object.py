# import datetime
from datetime import date

birthday = date(1991, 4, 12)
print(birthday)
print(type(birthday))

moon_landing = date(year = 1969, month = 7, day = 20)
print(moon_landing)

# date(2025, 15, 10)
# date(2020, 1, 35)

print(birthday.year)
print(birthday.month)
print(birthday.day)

# birthday.year = 2000

today = date.today()
print(today)
print(type(today))