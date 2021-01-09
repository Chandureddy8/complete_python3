# pillows = {
#     "soft": 79.99,
#     "hard": 99.99
# }

# print(pillows["soft"])
# print(pillows.__getitem__("soft"))

class CrayonBox():
    def __init__(self):
        self.crayons = []

    def add(self, crayon):
        self.crayons.append(crayon)

    def __getitem__(self, index):
        return self.crayons[index]

    def __setitem__(self, index, value):
        self.crayons[index] = value


cb = CrayonBox()
cb.add("Blue")
cb.add("Red")

print(cb[0])
print(cb[1])

cb[0] = "Yellow"

print(cb[0])

for crayon in cb:
    print(crayon)