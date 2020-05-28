from functools import reduce

l1 = list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))

l2 = list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))

res = reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])

print(l1,l2,res, type(res), sep="\n")


