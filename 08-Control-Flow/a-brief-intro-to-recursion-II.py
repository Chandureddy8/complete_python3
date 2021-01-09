# def reverse(str):
#     start_index = 0
#     last_index = len(str) - 1    # -1
#     reversed_string = ""         # warts

#     while last_index >= start_index:
#         reversed_string += str[last_index]
#         last_index -= 1

#     return reversed_string

def reverse(str):
    if len(str) <= 1:
        return str

    return str[-1] + reverse(str[:-1])

print(reverse("lsakdlsakdlskda")) # warts

# straw
# w + reverse(stra)
# w + a + reverse(str)
# w + a + r + reverse(st)
# w + a + r + t + reverse(s)
# w + a + r + t + s