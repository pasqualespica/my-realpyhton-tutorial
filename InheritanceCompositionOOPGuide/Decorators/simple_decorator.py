import functools

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper


# def say_whee():
#     print("Whee!")


# say_whee = my_decorator(say_whee)


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


# So, @my_decorator is just an easier way of saying 
# say_whee = my_decorator(say_whee). 
# It’s how you apply a decorator to a function.

@my_decorator
def say_whee():
    print("Whee!")
    
say_whee()

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

# @do_twice
# def stampa_due_volte():
#     print("Sono Anonimo !!!")
@do_twice
def stampa_due_volte():
    print("Sono Anonimo !!!")

stampa_due_volte()

# Decorating Functions With Arguments


@do_twice
def greet(variabile):
    print(f"Hello {variabile}")

greet("Pasquale Ciaooo ")


@do_twice
def greet_ext(variabile:str, lista:list, mappa:dict):
    print(f"Hello {variabile}")
    for e in lista :
        print(e)
    for k,v in mappa.items():
        print(k,v)

print(">>>>>>>>>>>>>.")
greet_ext("Passssss", (1,2,3), {"saldi":100 , "neg": "coop"})

print(greet_ext.__name__)
