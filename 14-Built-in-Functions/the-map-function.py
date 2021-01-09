numbers = [4, 8, 15, 16, 23, 42]
cubes = [number ** 3 for number in numbers]
print(cubes)

def cube(number):
    return number ** 3

print(list(map(cube, numbers)))

animals = ["cat", "bear", "zebra", "donkey", "cheetah"]
print(list(map(len, animals))) 