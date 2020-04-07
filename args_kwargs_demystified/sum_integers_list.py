# Using the Python args Variable in Function Definitions

# There are a few ways you can pass a varying number of arguments to a function. 
# The first way is often the most intuitive for people that have experience with collections.
# You simply pass a list or a set of all the arguments to your function. 
# So for my_sum(), you could pass a list of all the integers you need to add:


# sum_integers_list.py

def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))

# This implementation works, but whenever you call this function you’ll also need 
# to create a list of arguments to pass to it. 
# This can be inconvenient, especially if you don’t know up front all the values that should go into the list.
