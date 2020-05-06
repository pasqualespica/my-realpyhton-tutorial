import functools
from _24_class_count_stateful import CountCalls

# LRU Least recently used
# https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        # s1 = [repr(a) for a in args]
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            # print(f"PUT {func.__name__} {s1} in cache")
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        # print(f"GET {func.__name__} {s1} from cache")
        return wrapper_cache.cache[cache_key]
    # come here only one time
    wrapper_cache.cache = dict()
    return wrapper_cache


# @cache
@functools.lru_cache(maxsize=4)
@CountCalls
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

fibonacci(10)


# You can use the 
# .cache_info()
#  method to see how the cache performs, and you can tune it if needed. 
print(fibonacci.cache_info())