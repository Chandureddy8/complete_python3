class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivity > self.negativity

my_emotional_state = Emotion(positivity = 50, negativity = 75)

if my_emotional_state:
    print("This will NOT print because I have more negativity than positivity.")

my_emotional_state.positivity = 100

if my_emotional_state:
    print("This WILL print because I have more positivity than negativity")