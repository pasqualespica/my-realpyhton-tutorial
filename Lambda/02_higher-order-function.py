

high_ord_func = lambda x, func: x + func(x)

moltiplica = high_ord_func(2, lambda x: x * x)

somma3 = high_ord_func(2, lambda x: x + 3)

print(somma3, moltiplica, sep="\n")


# Python exposes higher-order functions as built-in functions or in the standard library. 
# 
# Examples include 
#   map(), 
#   filter(), 
#   functools.reduce(), 
# 
# as well as key functions like 
# 
#   sort(), 
#   sorted(), 
#   min(), and max(). 
# 
# You’ll use lambda functions together with Python higher-order functions in Appropriate Uses of Lambda Expressions.
