

add_one = lambda x: x + 1

print (add_one(3))

print((lambda x: x * 2)(5) )


#  Multi-argument functions
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'

print(full_name('guido', 'van rossum'))

