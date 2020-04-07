# Python args and kwargs: Demystified
https://realpython.com/python-kwargs-and-args/

Sometimes, when you look at a function definition in Python, you might see that it takes two strange arguments: *args and **kwargs. If you’ve ever wondered what these peculiar variables are, or why your IDE defines them in main(), then this article is for you. You’ll learn how to use args and kwargs in Python to add more flexibility to your functions.

*By the end of the article, you’ll know:*

* What *args and **kwargs actually mean
* How to use *args and **kwargs in function definitions
* How to use a single asterisk (*) to unpack iterables
* How to use two asterisks (**) to unpack dictionaries

## Passing Multiple Arguments to a Function
*args and **kwargs allow you to pass multiple arguments or keyword arguments to a function. Consider the following example. This is a simple function that takes two arguments and returns their sum:

```python
def my_sum(a, b):
    return a + b
```

Bear in mind that the iterable object you’ll get using the unpacking operator * is not a list but a tuple. A tuple is similar to a list in that they both support slicing and iteration. However, tuples are very different in at least one aspect: lists are mutable, while tuples are not. To test this, run the following code. This script tries to change a value of a list:

## Using the Python kwargs Variable in Function Definitions
Okay, now you’ve understood what *args is for, but what about **kwargs? **kwargs works just like *args, but instead of accepting positional arguments it accepts keyword (or named) arguments. Take the following example:


Note that in the example above the iterable object is a standard dict. If you iterate over the dictionary and want to return its values, like in the example shown, then you must use .values().

In fact, if you forget to use this method, you will find yourself iterating through the keys of your Python kwargs dictionary instead, like in the following example:

```python
# concatenate_keys.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the keys of the Python kwargs dictionary
    for arg in kwargs: # .values()
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
```

Now, if you try to execute this example, you’ll notice the following output:

```bash
$ python concatenate_keys.py
abcde
```

As you can see, if you don’t specify .values(), your function will iterate over the keys of your Python kwargs dictionary, returning the wrong result.

## Ordering Arguments in a Function
Now that you have learned what *args and **kwargs are for, you are ready to start writing functions that take a varying number of input arguments. But what if you want to create a function that takes a changeable number of both positional and named arguments?

In this case, you have to bear in mind that order counts. Just as non-default arguments have to precede default arguments, so *args must come before **kwargs.

To recap, the correct order for your parameters is:

1. Standard arguments
2. *args arguments
3. **kwargs arguments

For example, this function definition is correct

```python
# correct_function_definition.py
def my_function(a, b, *args, **kwargs):
    pass
```

The *args variable is appropriately listed before **kwargs. But what if you try to modify the order of the arguments? For example, consider the following function:

```python
# wrong_function_definition.py
def my_function(a, b, **kwargs, *args):
    pass
```

Now, **kwargs comes before *args in the function definition. If you try to run this example, you’ll receive an error from the interpreter:

```bash
$ python wrong_function_definition.py
  File "wrong_function_definition.py", line 2
    def my_function(a, b, **kwargs, *args):
                                    ^
SyntaxError: invalid syntax
```

In this case, since *args comes after **kwargs, the Python interpreter throws a SyntaxError.


## Unpacking With the Asterisk Operators: * & **


