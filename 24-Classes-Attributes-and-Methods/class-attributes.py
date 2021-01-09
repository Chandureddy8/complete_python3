class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        print(f"New Number of Counter objects created: {cls.count}")
        return two_counters

print(Counter.count)
c1 = Counter()
print(Counter.count)

c2, c3 = Counter.create_two()
print(Counter.count)

print(c1.count)
print(c2.count)
print(c3.count)