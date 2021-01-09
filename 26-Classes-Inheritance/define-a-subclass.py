class Store():
    def __init__(self):
        self.owner = "Boris"

    def exclaim(self):
        return "Lots of stuff to buy, come inside!"

class CoffeeShop(Store):
    pass

starbucks = CoffeeShop()

print(starbucks.owner)
print(starbucks.exclaim())