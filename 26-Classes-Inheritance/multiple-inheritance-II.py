class Restaurant():
    def make_reservation(self, party_size):
        print(f"Booked a table for {party_size}")

class Steakhouse(Restaurant):
    pass

class Bar():
    def make_reservation(self, party_size):
        print(f"Booked a lounge for {party_size}")

class BarAndGrill(Steakhouse, Bar):
    pass

bag = BarAndGrill()
bag.make_reservation(2)
print(BarAndGrill.mro())