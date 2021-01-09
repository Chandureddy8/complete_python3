class Pokemon():
    def __init__(self, name, specialty, health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("Raaaaarr!")

    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} Pokemon!")

    def take_damage(self, amount):
        self.health -= amount

squirtle = Pokemon("Squirtle", "Water")
charmander = Pokemon(name = "Charmander", specialty = "Fire", health = 110)
squirtle.roar()
charmander.roar()
squirtle.describe()
charmander.describe()
print(squirtle.health)
squirtle.take_damage(20)
print(squirtle.health)

squirtle.health = 60
print(squirtle.health)

print(charmander.health)
