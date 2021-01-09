from unittest.mock import Mock
from random import randint

def generate_number():
    return randint(1, 10)

call_me_maybe = Mock(return_value = 10, side_effect = generate_number)

# call_me_maybe.side_effect = generate_number
print(call_me_maybe())
print(call_me_maybe())
print(call_me_maybe())

three_item_list = Mock()
three_item_list.pop.side_effect = [3, 2, 1, IndexError("pop from empty list")]

print(three_item_list.pop())
print(three_item_list.pop())
print(three_item_list.pop())
# print(three_item_list.pop())

mock = Mock(side_effect = NameError("Some error message"))
mock.side_effect = None
print(mock())