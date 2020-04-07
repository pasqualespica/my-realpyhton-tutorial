# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    print(f" args arguemnt is a {type(kwargs)}")
    for arg in kwargs.values():
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))

# When you execute the script above, concatenate() will iterate through 
# the Python kwargs dictionary and concatenate all the values it finds:

# Like args, kwargs is just a name that can be changed to whatever you want. 
# Again, what is important here is the use of the unpacking operator(**).

