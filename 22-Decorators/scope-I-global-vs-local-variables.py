age = 28

def fancy_func():
    age = 100
    print(age)

fancy_func()
print(age)

TAX_RATE = 0.08

def calculate_tax(price):
    return round(price * TAX_RATE, 2)

def calculate_tip(price):
    return round(price * (TAX_RATE * 3), 2)

print(calculate_tax(10))
print(calculate_tip(10))
