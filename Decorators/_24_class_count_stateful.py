
import functools
# class Counter:
#     def __init__(self, start=0):
#         self.count = start

#     def __call__(self):
#         self.count += 1
#         print(f"Current count is {self.count}")

#  =================================

# Recall that the decorator syntax @my_decorator is 
# just an easier way of saying 
# func = my_decorator(func).
#  Therefore, if my_decorator is a class, it needs to take
#  func as an argument in its 
# .__init__() method. Furthermore, 
# the class needs to be callable so that it can 
# stand in for the decorated function.

# The .__call__() method is executed each time you try to call an instance 
# of the class:


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print("Whee!")

if __name__ == "__main__":
    for _ in range(5):
        say_whee()
