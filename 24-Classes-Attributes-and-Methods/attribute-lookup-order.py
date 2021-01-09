class Example():
    data = "Class attribute!"

e1 = Example()
e2 = Example()
print(e1.data)
print(e2.data)

e1.data = "Instance attribute!"
print(e1.data)
print(e2.data)

del e1.data
print(e1.data)
print(e2.data)

# print(e1.nonsense)