# Sometimes, it’s useful to pass arguments to your decorators. 
# For instance, @do_twice could be extended to a @repeat(num_times) decorator. 
# The number of times to execute the decorated function could then be given as an argument.
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("GRANDE WORLD!!")