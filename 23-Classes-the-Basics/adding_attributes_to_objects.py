class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! This object is {self}")

acoustic = Guitar()
electric = Guitar()

acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"

print(acoustic.wood)
print(electric.nickname)

# print(electric.year)
# print(acoustic.nickname)