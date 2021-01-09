class Guitar():
    def __init__(self, wood):
        self.wood = wood
        
acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood)
print(electric.wood)

baritone = Guitar("Alder")

print(baritone.wood)

print(acoustic)
print(baritone)

a = [1, 2, 3]
b = [1, 2, 3]
