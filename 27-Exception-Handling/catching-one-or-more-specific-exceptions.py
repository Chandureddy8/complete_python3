def divide_5_by_number(n):
    try:
        calculation = 5 / n
    except (ZeroDivisionError, TypeError) as e:
        return f"Something went wrong. The error was {e}"
    return calculation

print(divide_5_by_number(10))
print(divide_5_by_number(0))
print(divide_5_by_number("nonsense"))