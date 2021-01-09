class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise StupidMistake("Extra stupid mistake")
except StupidMistake as e:
    print(f"Caught the error: {e}")

try:
    raise StupidMistake("Extra stupid mistake")
except Mistake as e:
    print(f"Caught the error: {e}")

try:
    raise SillyMistake("Super silly mistake")
except Mistake as e:
    print(f"Caught the error: {e}")