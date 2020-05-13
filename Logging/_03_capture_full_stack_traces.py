"""
The logging module also allows you to capture the full stack traces in an 
application. Exception information can be captured if the `exc_info` parameter 
is passed as True, and the logging functions are called like this:

https://realpython.com/python-exceptions/

"""
import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
