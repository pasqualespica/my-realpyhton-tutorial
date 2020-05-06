def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


#   So, @my_decorator is just an easier way of saying 
#   say_whee = my_decorator(say_whee). 
#   It’s how you apply a decorator to a function.
@my_decorator
def say_whee():
    print("Whee!")

say_whee()
