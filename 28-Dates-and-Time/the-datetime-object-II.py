from datetime import datetime

today = datetime.today()

print(today.strftime("%m"))
print(today.strftime("%m %d"))
print(today.strftime("%m/%d/%Y"))
print(today.strftime("%m-%d-%Y"))

print(today.strftime("%Y-%m-%d"))
print(today.strftime("%y-%m-%d"))

print(today.strftime("%A"))
print(today.strftime("%B"))