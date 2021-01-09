bubble_tea_flavors = [
    ["Honeydew", "Mango", "Passion Fruit"],
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
]

# print(len(bubble_tea_flavors))
# print(bubble_tea_flavors[0])
# print(bubble_tea_flavors[1])
# print(bubble_tea_flavors[-1])
# print(len(bubble_tea_flavors[1]))

# print(bubble_tea_flavors[1][2])
# print(bubble_tea_flavors[0][0])
# print(bubble_tea_flavors[2][1])

all_flavors = []

for flavor_pack in bubble_tea_flavors:
    for flavor in flavor_pack:
        all_flavors.append(flavor)

print(all_flavors)