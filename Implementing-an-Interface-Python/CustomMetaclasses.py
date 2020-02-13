

class Foo:
    pass


f = Foo()


"""

The expression Foo() creates a new instance of class Foo. 
When the interpreter encounters Foo(), the following occurs:

The __call__() method of Foo’s parent class is called. 
Since Foo is a standard new-style class, 
its parent class is the type metaclass, 
so type’s __call__() method is invoked.

That __call__() method in turn invokes the following:

__new__()
__init__()


If Foo does not define __new__() and __init__(), default methods are inherited from Foo’s ancestry. But if Foo does define these methods, they override those from the ancestry, which allows for customized behavior when instantiating Foo.

In the following, a custom method called new() is defined and assigned as the __new__() method for Foo


"""


def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new

f = Foo()
print(f.attr)


g = Foo()
print(g.attr)


class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr =200100
        return x


class Foo(metaclass=Meta):
    pass


print(Foo.attr)


# Object Factory:
class Foo:
    def __init__(self):
        self.attr = 100


x = Foo()
x.attr


y = Foo()
y.attr


z = Foo()
z.attr



# Class Factory:
class Meta(type):
    def __init__(
        cls, name, bases, dct
    ):
        cls.attr = 100


class X(metaclass=Meta):
    pass


X.attr


class Y(metaclass=Meta):
    pass


Y.attr


class Z(metaclass=Meta):
    pass


Z.attr


"""

Is This Really Necessary?
As simple as the above class factory example is, it is the essence of how metaclasses work. They allow customization of class instantiation.

Still, this is a lot of fuss just to bestow the custom attribute attr on each newly created class. Do you really need a metaclass just for that?

In Python, there are at least a couple other ways in which effectively the same thing can be accomplished:

"""

# Simple Inheritance:
class Base:
    attr = 100


class X(Base):
    pass


class Y(Base):
    pass


class Z(Base):
    pass


X.attr

Y.attr

Z.attr


# Class Decorator:
def decorator(cls):
    class NewClass(cls):
        attr = 100
    return NewClass


@decorator
class X:
    pass


@decorator
class Y:
    pass


@decorator
class Z:
    pass


X.attr

Y.attr

Z.attr
