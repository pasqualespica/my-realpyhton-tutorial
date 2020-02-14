
"""
Every list comprehension in Python includes three elements:

expression is the member itself, a call to a method, 
or any other valid expression that returns a value. 
In the example above, the expression i * i is the square of the member value.

member is the object or value in the list or iterable. 
In the example above, the member value is i.

iterable is a list, set, sequence, generator, 
or any other object that can return its elements one at a time. 
In the example above, the iterable is range(10).

"""
# new_list = [expression for member in iterable]


# >> Ex.1  Using for Loops

import random
squares = []
for i in range(10):
    squares.append(i * i)

# with list comprehension
squares = [i * i for i in range(10)]



# >> Ex. 2 Using map() Objects

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08
def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)

final_prices = map(get_price_with_tax, txns)

print (type(final_prices))


l = list(final_prices)

print(l)

# with list comprehension
final_prices = [get_price_with_tax(i) for i in txns]


# How to Supercharge Your Comprehensions

# Using Conditional Logic

# new_list = [expression for member in iterable(if conditional)]

# new_list = [expression(if conditional) for member in iterable]


"""
Using Set and Dictionary Comprehensions

While the list comprehension in Python is a common tool, 
you can also create set and dictionary comprehensions. 
A set comprehension is almost exactly the same as a list 
comprehension in Python. 
The difference is that set comprehensions make sure the output 
contains no duplicates. You can create a set comprehension 
by using curly braces instead of brackets:

"""
# SET
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)

# DICT
# Dictionary comprehensions are similar, 
# with the additional requirement of defining a key:
squares = {i: i * i for i in range(10)}
print(squares)


# Using the Walrus Operator


def get_weather_data():
    return random.randrange(90, 110)


# The formula expression for member in iterable(if conditional) 
# provides no way for the conditional to assign data to a variable 
# that the expression can access.

# The walrus operator solves this problem. 
# It allows you to run an expression while

print("walrus operator...3.8.....")

hot_temps = [temp for _ in range(20) if (temp:=get_weather_data()) >= 100]

print (hot_temps)

matrice_count = [[ i for e in range(i)] for i in range(5)]

print(*matrice_count, sep="\n")

matrix = [ 
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2],
    ]

flat = [num for row in matrix for num in row]

print(flat)

#  Choose Generators for Large Datasets

print(sum([i * i for i in range(1000)]))
