user_value = input("Enter a temperature in Fahrenheit to convert to Celsius ")
fahr_temp = float(user_value)
cels_temp = (fahr_temp - 32) * (5/9)
print(fahr_temp, "in Celsius is", cels_temp)