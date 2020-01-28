

# In Python, functions are first-class objects
def yell(text):
    return text.upper() + '!'

# >> Functions Are Objects
# Because the yell function is an object in Python 
# you can assign it to another variable, just like any other object:
bark = yell
bark('woof')
del yell
# >> > yell('hello?')
# NameError: "name 'yell' is not defined"

# >> > bark('hey')
# 'HEY!'
bark.__name__

# >> Functions Can Be Stored In Data Structures
# As functions are first-class citizens you can store them 
# in data structures, just like you can with other objects. 
# For example, you can add functions to a list:
# funcs = [bark, str.lower, str.capitalize]
funcs = [bark, str.lower, str.capitalize]
for f in funcs:
    print(f, f('hey there'))

# >> Functions Can Be Passed To Other Functions
# Because functions are objects you can pass them as 
# arguments to other functions. Here’s a greet function
#  that formats a greeting string using the function object
#  passed to it and then prints it:
def greet(func):
    greeting = func('Hi, I am a Python program')
    print(greeting)


# >> > funcs[0]('heyho')
# 'HEYHO!'

# Functions Can Be Nested
# Python allows functions to be defined inside other functions. T
# hese are often called nested functions or inner functions.
#  Here’s an example:
def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)
