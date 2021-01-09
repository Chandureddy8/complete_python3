from datetime import datetime

# import datetime
# datetime.datetime

print(datetime(1999, 7, 24))
print(datetime(1999, 7, 24, 14))
print(datetime(1999, 7, 24, 14, 16))
print(datetime(1999, 7, 24, 14, 16, 58))
print(datetime(year = 1999, month = 7, day = 24, hour = 14, minute = 16, second = 58))

today = datetime.today()
print(today)
print(datetime.now())
print(today.year)
print(today.month)
print(today.day)
print(today.hour)
print(today.minute)
print(today.second)

print(today.weekday())

same_time_twenty_years_ago = today.replace(year = 1999)
print(same_time_twenty_years_ago)

same_time_in_january = today.replace(month = 1)
print(same_time_in_january)

start_of_january_1999 = today.replace(year = 1999, month = 1, day = 1)
print(start_of_january_1999)
