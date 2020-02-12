import functools
from flask import Flask, g, request, redirect, url_for
import random
from timer_wrap import debug, timer
import math
import time
from simple_decorator import do_twice

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(99)


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


make_greeting("Benjamin")
make_greeting(name="Dorrisile", age=116)

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


approximate_e(5)

# Registering Plugins
# Decorators don’t have to wrap the function they’re decorating. 
# They can also simply register that a function exists and return it
#  unwrapped. This can be used, for instance, to create a 
# light-weight plug-in architecture:
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


app = Flask(__name__)


def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required


@app.route("/secret")
@login_required
def secret():
    pass


@timer
class TimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num
        time.sleep(1)

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])

# Decorating a class does not decorate its methods. 
# Recall that @timer is just shorthand for 
# TimeWaster = timer(TimeWaster).
# Here, @timer only measures the time it takes to instantiate the class:

tw = TimeWaster(1000)

# Nesting Decorators
@debug
@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Evaaaaa")
