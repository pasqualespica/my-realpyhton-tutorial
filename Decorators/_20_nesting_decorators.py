# from decorators import debug, do_twice

from _06_do_twice_args_kwargs_and_return_functools import do_twice
from _12_debugging_code import debug


# @debug
# @do_twice
@do_twice
@debug
def greet(name):
    print(f"Hello {name}")


greet("CIAOOO PASQUALE !!!")
