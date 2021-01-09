class Person():
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __len__(self):
        return self.height

values = [
    "Boris",
    [1, 2, 3],
    (4, 5, 6, 7),
    { "a": 1, "b": 2},
    Person(name = "Boris", height = 71)
]

for value in values:
    print(len(value))