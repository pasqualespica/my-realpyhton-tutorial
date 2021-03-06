# How to Use Python Lambda Functions

https://realpython.com/python-lambda/#alternatives-to-lambdas



**Reduction** is a lambda calculus strategy to compute the value of the expression. It consists of substituting the argument 2 for x:

```python
(lambda x: x + 1)(2) = lambda 2: 2 + 1
                     = 2 + 1
                     = 3
```


The `dis` module exposes functions to analyze Python bytecode generated by the Python compiler:
https://docs.python.org/3/library/dis.html

```py
>>> import dis
>>> add = lambda x, y: x + y
>>> type(add)
<class 'function'>
>>> dis.dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
>>> add
<function <lambda> at 0x7f30c6ce9ea0>

```

Now see it with a `regular function` object:

```py
>>> import dis
>>> def add(x, y): return x + y
>>> type(add)
<class 'function'>
>>> dis.dis(add)
  1           0 LOAD_FAST                0 (x)
              2 LOAD_FAST                1 (y)
              4 BINARY_ADD
              6 RETURN_VALUE
>>> add
<function add at 0x7f30c6ce9f28>
```



## Syntax
As you saw in the previous sections, a `lambda form` presents syntactic distinctions from a normal function. 
In particular, a lambda function has the following characteristics:

1. It can only contain expressions and can’t include statements in its body.
2. It is written as a single line of execution.
3. It does not support type annotations.
4. It can be immediately invoked (IIFE).


## Arguments
Like a normal function object defined with def, Python lambda expressions support all the different ways of passing arguments. This includes:

1. Positional arguments
2. Named arguments (sometimes called keyword arguments)
3. Variable list of arguments (often referred to as varargs)
4. Variable list of keyword arguments
5. Keyword-only arguments
