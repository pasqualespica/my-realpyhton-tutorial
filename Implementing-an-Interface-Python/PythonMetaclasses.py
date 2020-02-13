# Defining a Class Dynamically


# You can also call type()
#  with three arguments—type( < name > , < bases > , < dct > ):

# <name > 
# specifies the class name. 
# This becomes the __name__ attribute of the class.

# <bases > 
# specifies a tuple of the base classes 
# from which the class inherits. This becomes the __bases__ attribute of the class.

# <dct > specifies a namespace dictionary containing 
# definitions for the class body. 
# This becomes the __dict__ attribute of the class.


# Example 1

# In this first example, the < bases > and < dct > 
# arguments passed to type() are both empty. No inheritance 
# from any parent class is specified, and nothing is initially 
# placed in the namespace dictionary. 
# This is the simplest class definition possible:

Foo = type('Foo', (), {})

x = Foo()
print(x)


# Example 2

# Here, < bases > is a tuple with a single element Foo, 
# specifying the parent class that Bar inherits from. 
# An attribute, attr, is initially placed into the namespace dictionary:
Bar = type('Bar', (Foo,), dict(attr=100))

x = Bar()
print(x.attr)
print(x.__class__)
print(x.__class__.__bases__)


# class Bar(Foo):
#     attr = 100


# x = Bar()
# x.attr
# x.__class__
# x.__class__.__bases__


# Example 3

# This time, < bases > is again empty. 
# Two objects are placed into the namespace dictionary 
# via the < dct > argument. 
# The first is an attribute named attr and 
# the second a function named attr_val, which becomes a 
# method of the defined class:

Foo = type(
    'Foo',
    (),
    {
        'attr': 100,
        'attr_val': lambda x: x.attr
    }
)

x = Foo()
x.attr

x.attr_val()


# class Foo:
#     attr = 100
#     def attr_val(self):
#         return self.attr

# x = Foo()
# x.attr
# x.attr_val()


# Example 4

# Only very simple functions can be defined with lambda in Python. 
# In the following example, a slightly more complex 
# function is defined externally then assigned to attr_val 
# in the namespace dictionary via the name f:

def f(obj):
    print('attr =', obj.attr)


Foo = type(
    'Foo',
    (),
    {
        'attr': 100,
        'attr_val': f
    }
)

x = Foo()
x.attr

x.attr_val()


# def f(obj):
#     print('attr =', obj.attr)

# class Foo:
#     attr = 100
#     attr_val = f

# x = Foo()
# x.attr
# x.attr_val()


