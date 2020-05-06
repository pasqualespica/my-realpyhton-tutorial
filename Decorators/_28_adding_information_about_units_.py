# The following example is somewhat similar to the Registering Plugins 
# example from earlier, in that it does not really change the behavior of 
# the decorated function. Instead, it simply adds "unit" as a function attribute:

import math

def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit


# https: // www.python.org/dev/peps/pep-3107/
@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height


print(volume(3,5), volume.unit)
