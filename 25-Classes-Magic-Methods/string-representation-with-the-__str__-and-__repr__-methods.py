class Card():
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return f"{self._rank} of {self._suit}"

    def __repr__(self):
        return f'Card("{self._rank}", "{self._suit}")'

c = Card("Ace", "Spades")
print(c)
print(str(c))
print(repr(c))