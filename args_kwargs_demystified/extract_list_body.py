# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6, 7]

a, *b, c = my_list

print(f"a {a} type {type(a)}")
print(f"b {b} type {type(b)}")
print(f"c {c} type {type(c)}")

# NOTE SyntaxError: two starred expressions in assignment
