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

You are now able to use *args and **kwargs to define Python functions that take
 a varying number of input arguments.
  Let’s go a little deeper to understand something more about the **unpacking operators**.

https://www.python.org/dev/peps/pep-0448/


The single and double asterisk unpacking operators were introduced in Python 2. As of the 3.5 release, they have become even more powerful, thanks to PEP 448. In short, the unpacking operators are operators that unpack the values from iterable objects in Python. 

- The single asterisk operator * can be used on any iterable that Python provides,  
while 
- the double asterisk operator ** can only be used on dictionaries.

```python
# print_list.py
my_list = [1, 2, 3]
print(my_list)
```
This code defines a list and then prints it to the standard output:

```bash
$ python print_list.py
[1, 2, 3]
```
Note how the list is printed, along with the corresponding brackets and commas.

Now, try to prepend the unpacking operator * to the name of your list:

```python
# print_unpacked_list.py
my_list = [1, 2, 3]
print(*my_list)
Here, the * operator tells print() to unpack the list first.
```

In this case, the output is no longer the list itself, but rather the content of the list:

```bash
$ python print_unpacked_list.py
1 2 3
```
*Can you see the difference between this execution and the one from print_list.py? Instead of a list, print() has taken three separate arguments as the input.*

You can also use this method to call your own functions, but if your function requires a specific number of arguments, then the iterable you unpack must have the same number of arguments.

To test this behavior, consider this script:

```python
# unpacking_call.py
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3]
my_sum(*my_list)
```

Here, `my_sum()` explicitly states that a, b, and c are required arguments.

If you run this script, you’ll get the sum of the three numbers in my_list:

```bash
$ python unpacking_call.py
6
```

The 3 elements in my_list match up perfectly with the required arguments in my_sum().

Now look at the following script, where my_list has 4 arguments instead of 3:

```python
# wrong_unpacking_call.py
def my_sum(a, b, c):
    print(a + b + c)

my_list = [1, 2, 3, 4]
my_sum(*my_list)
```
In this example, my_sum() still expects just three arguments, but the * operator gets 4 items from the list. If you try to execute this script, you’ll see that the Python interpreter is unable to run it:

```bash
$ python wrong_unpacking_call.py
Traceback (most recent call last):
  File "wrong_unpacking_call.py", line 6, in <module>
    my_sum(*my_list)
TypeError: my_sum() takes 3 positional arguments but 4 were given
```

When you use the * operator to unpack a list and pass arguments to a function, it’s exactly as though you’re passing every single argument alone. 
This means that you can use **multiple unpacking operators** to get values from several lists and pass them all to a single function.

To test this behavior, consider the following example `sum_integers_args_3.py`

If you run this example, all three lists are unpacked. Each individual item is passed to my_sum(), resulting in the following output:

```bash
$ python sum_integers_args_3.py
45
```

There are other convenient uses of the unpacking operator. For example, say you need to split a list into three different parts. The output should show the first value, the last value, and all the values in between. With the unpacking operator, you can do this in just one line of code `extract_list_body.py`

In this example, my_list contains 6 items. The first variable is assigned to a, the last to c, and all other values are packed into a new list b. If you run the script, print() will show you that your three variables have the values you would expect:

```bash
$ python extract_list_body.py
1
[2, 3, 4, 5]
6
```

Another interesting thing you can do with the unpacking operator * is to split the items of any iterable object. This could be very useful if you need to merge two lists, for instance: `merging_lists.py`

The unpacking operator * is prepended to both my_first_list and my_second_list.

If you run this script, you’ll see that the result is a merged list:

```bash
$ python merging_lists.py
[1, 2, 3, 4, 5, 6]
```

You can even **merge** two different **dictionaries** by using the unpacking operator **: `merging_dicts.py`

Here, the iterables to merge are my_first_dict and my_second_dict.

Executing this code outputs a merged dictionary:

```bash
$ python merging_dicts.py
{'A': 1, 'B': 2, 'C': 3, 'D': 4}
```

Remember that the * operator works on any iterable object. It can also be used to unpack a string:

```
# string_to_list.py
a = [*"RealPython"]
print(a)
````
In Python, strings are iterable objects, so * will unpack it and place all individual values in a list a:

```bash
$ python string_to_list.py
['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']
```

The previous example seems great, but when you work with these operators it’s important to keep in mind the seventh rule of The Zen of Python by Tim Peters: Readability counts.

To see why, consider the following example:

```python
# mysterious_statement.py
*a, = "RealPython"
print(a)
```

There’s the unpacking operator *, followed by a variable, a comma, and an assignment. That’s a lot packed into one line! In fact, this code is no different from the previous example. It just takes the string RealPython and assigns all the items to the new list a, thanks to the unpacking operator *.

**The comma after the `a` does the trick.** 
When you use the unpacking operator with variable assignment, Python requires that your resulting variable is either a list or a tuple. With the trailing comma, you have actually defined a tuple with just one named variable a.

```bash
>>> *a = "RealPython"
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
```

While this is a neat trick, many Pythonistas would not consider this code to be very readable. As such, it’s best to use these kinds of constructions sparingly.









