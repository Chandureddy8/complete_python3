foods = "Sushi", "Steak", "Guacamole"
foods = ("Sushi", "Steak", "Guacamole")

print(type(foods))

empty = ()
print(type(empty))

# mystery = (1)
# print(type(mystery))
mystery = 1,
print(type(mystery))

mystery = (1, )
print(type(mystery))

print(tuple(["Sushi", "Steak", "Guacamole"]))
print(type(tuple(["Sushi", "Steak", "Guacamole"])))

print(tuple(["abc"]))