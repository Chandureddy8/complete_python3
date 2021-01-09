from unittest.mock import Mock, MagicMock

plain_mock = Mock()
magic_mock = MagicMock()

# print(len(plain_mock)) # __len__
print(len(magic_mock))

# print(plain_mock[3])

print(magic_mock[3])
print(magic_mock[100])
print(magic_mock["hello"])
# __getitem__

magic_mock.__len__.return_value = 50
print(len(magic_mock))

if magic_mock:
    print("hello")

magic_mock.__bool__.return_value = False

if magic_mock:
    print("goodbye")

magic_mock.__getitem__.return_value = 100
print(magic_mock[3])
print(magic_mock[100])
print(magic_mock["hello"])