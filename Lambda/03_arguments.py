

# Positional arguments
print((lambda x, y, z: x + y + z)(1, 2, 3))

# default values
print((lambda x, y, z=3: x + y + z)(1, 2))

# Named arguments(sometimes called keyword arguments)
print((lambda x, y, z=3: x + y + z)(1, y=2))

# Variable list of arguments(often referred to as varargs)
print((lambda *args: sum(args))(1, 2, 3))

# Variable list of keyword arguments
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))

# Keyword-only arguments
print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))
