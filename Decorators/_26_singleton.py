import functools


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


# Note: Singleton classes are not really used as often in Python 
# as in other languages. The effect of a singleton is usually better 
# implemented as a global variable in a module.


obj1 = TheOne()
obj2 = TheOne()

print(obj1 is obj2)

