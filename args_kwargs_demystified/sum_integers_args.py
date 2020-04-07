# sum_integers_args.py
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    print(f" args arguemnt is a {type(args)}")
    for x in args:
        result += x
    return result


print(my_sum(1, 2, 3))

# In this example, you’re no longer passing a list to my_sum(). 
# Instead, you’re passing three different positional arguments. my_sum() 
# takes all the parameters that are provided in the input and packs them all 
# into a single iterable object named args.

# The function still works, even if you pass the iterable object 
# as integers instead of args. All that matters here is that you use the unpacking operator(*).
