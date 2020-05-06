
from _06_do_twice_args_kwargs import do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")

greet("WORLD")
