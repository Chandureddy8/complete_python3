def outer():
    # Enclosing function scope

    def inner():
        # Local scope
        return len

    return inner()

print(outer()("python"))