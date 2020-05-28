
# In a normal function, n is evaluated at definition time,
# when the function is added to the list: funcs.append(wrap(n)).
print("evaluated at definition time . EX ...")
def wrap(n):
    def f():
        print(n)
    return f


numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()

# The unexpected result occurs because the free variable n, 
# as implemented, is bound at the execution time of the lambda expression. 
# The Python lambda function is a closure that captures n, a free variable bound at runtime. 
# At runtime, while invoking the function f on line 7, the value of n is three.
print("is bound at the execution time . EX ...")

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()
