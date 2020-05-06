
# Decorators don’t have to wrap the function they’re decorating. 
# They can also simply register that a function exists and return it unwrapped. 
# This can be used, for instance, to create a light-weight plug-in architecture

import random
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

for _ in range(10):
    randomly_greet("PASQUALINO...")