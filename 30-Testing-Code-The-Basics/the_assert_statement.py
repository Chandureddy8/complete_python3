def add(x, y):
  assert isinstance(x, int) and isinstance(y, int), "Both arguments must be integers"
  return x + y

print(add(3, 5))
# print(add(3, "5"))