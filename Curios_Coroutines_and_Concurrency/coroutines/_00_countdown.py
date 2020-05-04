# countdown.py
#
# A simple generator function


# A generator is a function that produces a sequence of results 
# instead of a single value

def countdown(n):
    print(f"Counting down from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Done counting down")


# Instead of returning a value, you generate a series of 
# values(using the yield statement)

# Typically, you hook it up to a for-loop

# Example use
if __name__ == '__main__':
    # Calling a generator function creates an generator object. 
    # However, it does not start running the function.
    for i in countdown(10):
        print(i)
