import functools

# ---------------------------
# MAP -----------------------
# ---------------------------

cap1 = list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))

print(cap1)

'''
You need to invoke list() to convert the iterator returned by map() 
into an expanded list that can be displayed in the Python shell interpreter.

Using a list comprehension eliminates the need for defining and invoking the lambda function:
'''

cap2 = [x.capitalize() for x in ['cat', 'dog', 'cow']]

print(cap2)


# ---------------------------
# FILTER --------------------
# ---------------------------

''' nunmeri pari '''
even = lambda x: x%2 == 0
pari_1 = list(filter(even, range(11)))
print(pari_1)

pari_2 = [x for x in range(11) if x % 2 == 0]
print(pari_2)

# ---------------------------
# REDUCE --------------------
# ---------------------------

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
somma = functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)
print (f"La somma e' {somma}")


''' A more idiomatic approach using a generator expression, as an argument to sum() in the example, is the following: '''
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
somma2 = sum(x[0] for x in pairs)
print(f"La somma e' {somma2}")

''' A slightly different and possibly cleaner solution removes ...  use unpacking: '''
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
somma3 = sum(x for x, _ in pairs)
print(f"La somma e' {somma3}")
