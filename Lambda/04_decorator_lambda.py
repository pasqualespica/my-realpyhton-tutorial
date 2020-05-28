# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)

    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2


# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))


# Decorating the lambda function this way could be useful for debugging purposes, possibly to debug the behavior of a 
# lambda function used in the context of a higher-order function or a key function. Let’s see an example with map():
print("\n Quadrati con MAP + LAMBDA + DECORATOR ")
lista_quadrati = list(map(trace(lambda x: x*2), range(3)))
print(lista_quadrati)