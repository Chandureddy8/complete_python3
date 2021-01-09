def outer():
    bubble_tea_flavor = "Black"

    def inner():
        nonlocal bubble_tea_flavor
        bubble_tea_flavor = "Taro"

    inner()

    return bubble_tea_flavor

print(outer())