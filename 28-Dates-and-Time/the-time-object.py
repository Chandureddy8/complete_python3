# import datetime
# datetime.time
from datetime import time

start = time()
print(start)
print(type(start))
print(start.hour)
print(start.minute)
print(start.second)

print(time(6))
print(time(hour = 6))
print(time(hour = 18))

print(time(12, 25))
print(time(hour = 12, minute = 25))

# 11:34:22PM
print(time(23, 34, 22))
evening = time(hour = 23, minute = 34, second = 22)
print(evening.hour)
print(evening.minute)
print(evening.second)

# time(27) 