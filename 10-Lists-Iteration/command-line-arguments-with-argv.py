import sys

# print(sys.argv)
# print(type(sys.argv))

word_lengths = 0

for arg in sys.argv[1:]:
    word_lengths += len(arg)

print(f"The total length of all command-line arguments is {word_lengths}")