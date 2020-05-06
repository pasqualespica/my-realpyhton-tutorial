import math
from _12_debugging_code import debug

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


approximate_e(5)