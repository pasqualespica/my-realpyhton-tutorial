import functools


# The state—the number of calls to the function—is stored in the 
# function attribute .num_calls 
# on the wrapper function.

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls


@count_calls
def say_whee():
    print("Whee!")

for _ in range(5):
    say_whee()
