mountains = ["Mount Everest", "K2"]
print(mountains)

mountains.extend(["Kangchenjunga", "Lhotse", "Makalu"])
print(mountains)

extra_mountains = ["Cho Oyu", "Dhaulagiri"]
mountains.extend(extra_mountains)
print(mountains)

mountains.extend([])
print(mountains)

steaks = ["Tenderloin", "New York Strip"]
more_steaks = ["T-Bone", "Ribeye"]

my_meal = steaks + more_steaks
print(my_meal)
print(steaks)
print(more_steaks)

steaks += more_steaks
print(steaks)