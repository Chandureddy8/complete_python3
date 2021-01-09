import unittest

class Address():
    def __init__(self, city, state):
        self.city = city
        self.state = state

class Owner():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Restaurant():
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner

    @property
    def owner_age(self):
        return self.owner.age

    def summary(self):
        return f"This restaurant is owned by {self.owner.name} and is located in {self.address.city}."

class TestRestaurant(unittest.TestCase):
    def setUp(self):
        print("This will run before each test!")
        address = Address(city = "New York", state = "New York")
        owner = Owner(name = "Jackie", age = 60)
        self.golden_palace = Restaurant(address, owner)

    def tearDown(self):
        print("This will run after each test!")

    def test_owner_age(self):
        self.assertEqual(self.golden_palace.owner_age, 60)

    def test_summary(self):
        self.assertEqual(
            self.golden_palace.summary(),
            "This restaurant is owned by Jackie and is located in New York."
        )







if __name__ == "__main__":
    unittest.main()