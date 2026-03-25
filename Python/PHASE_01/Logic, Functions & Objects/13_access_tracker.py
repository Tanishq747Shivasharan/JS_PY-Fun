# Closures & Nested Functions
def create_tracker():
    count = 0   # outer variable

    def tracker():
        nonlocal count
        count += 1
        return count

    return tracker

t = create_tracker()
print(t())
print(t())
