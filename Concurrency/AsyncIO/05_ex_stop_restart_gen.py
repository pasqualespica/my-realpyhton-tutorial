from itertools import cycle


def endless():
    """Yields 9, 8, 7, 6, 9, 8, 7, 6, ... forever"""
    yield from cycle((9, 8, 7, 6))


e = endless()
total = 0
for i in e:
    if total < 30:
        print(i, end=" ")
        total += i
    else:
        print()
        # Pause execution. We can resume later.
        break


# Resume
print("Resume....")
print(next(e))
print(next(e))
print(next(e))

