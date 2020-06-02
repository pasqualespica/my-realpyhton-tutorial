# Python Type Checking (Guide)

https://realpython.com/python-type-checking/#hello-types

### usefull links
http://mypy-lang.org/

Python supports the concept of gradual typing
https://www.python.org/dev/peps/pep-0483/


## Type Systems


### Dynamic Typing
Python is a dynamically typed language. This means that the Python interpreter does type checking only as code runs, and that the type of a variable is allowed to change over its lifetime. The following dummy examples demonstrate that Python has dynamic typing:
```py
>>> if False:
...     1 + "two"  # This line never runs, so no TypeError is raised
... else:
...     1 + 2
...
3

>>> 1 + "two"  # Now this is type checked, and a TypeError is raised
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```


```py
>>> thing = "Hello"
>>> type(thing)
<class 'str'>

>>> thing = 28.1
>>> type(thing)
<class 'float'>
```

### Static Typing
The opposite of dynamic typing is static typing. Static type checks are performed without running the program. In most statically typed languages, for instance C and Java, this is done as your program is compiled.

With static typing, variables generally are not allowed to change types, although mechanisms for casting a variable to a different type may exist.

Let’s look at a quick example from a statically typed language. Consider the following Java snippet:

```java
String thing;
thing = "Hello";
```


### Duck Typing
Another term that is often used when talking about Python is duck typing. This moniker comes from the phrase **“if it walks like a duck and it quacks like a duck, then it must be a duck”** (or any of its variations).

As an example, you can call len() on any Python object that defines a `.__len__()` method:

```py
>>> class TheHobbit:
...     def __len__(self):
...         return 95022
...
>>> the_hobbit = TheHobbit()
>>> len(the_hobbit)
95022
```

Note that the call to len() gives the return value of the` .__len__()` method. In fact, the implementation of `len()` is essentially equivalent to the following:

```py
def len(obj):
    return obj.__len__()
```


### Function Annotations
For functions, you can annotate arguments and the return value. This is done as follows:
```py
def func(arg: arg_type, optarg: arg_type = default) -> return_type:
    ...
```

The following simple example adds annotations to a function that calculates the circumference of a circle:
```py
import math

def circumference(radius: float) -> float:
    return 2 * math.pi * radius
```

When running the code, you can also inspect the annotations. They are stored in a special `.__annotations__` attribute on the function:

```py
>>> circumference(1.23)
7.728317927830891

>>> circumference.__annotations__
{'radius': <class 'float'>, 'return': <class 'float'>}

```

```py
# reveal.py

import math
reveal_type(math.pi)

radius = 1
circumference = 2 * math.pi * radius
reveal_locals()
```

Next, run this code through Mypy:
```bash
$ mypy reveal.py
reveal.py:4: error: Revealed type is 'builtins.float'

reveal.py:8: error: Revealed local types are:
reveal.py:8: error: circumference: builtins.float
reveal.py:8: error: radius: builtins.int

```

### Variable Annotations

```py
pi: float = 3.142

def circumference(radius: float) -> float:
    return 2 * pi * radius
```
Annotations of variables are stored in the module level __annotations__ dictionary:

```py
>>> circumference(1)
6.284

>>> __annotations__
{'pi': <class 'float'>}

```

### Type Comments
As mentioned, annotations were introduced in Python 3, and they’ve not been backported to Python 2. This means that if you’re writing code that needs to support legacy Python, you can’t use annotations.

Instead, you can use type comments. These are specially formatted comments that can be used to add type hints compatible with older code. To add type comments to a function you do something like this:
```py
import math

def circumference(radius):
    # type: (float) -> float
    return 2 * math.pi * radius
```

Type comments are handled directly by the type checker, so these types are not available in the __annotations__ dictionary:
```py
>>> circumference.__annotations__
{}
```

A type comment must start with the type: literal, and be on the same or the following line as the function definition. If you want to annotate a function with several arguments, you write each type separated by comma:
```py
def headline(text, width=80, fill_char="-"):
    # type: (str, int, str) -> str
    return f" {text.title()} ".center(width, fill_char)

print(headline("type comments work", width=40))
```

