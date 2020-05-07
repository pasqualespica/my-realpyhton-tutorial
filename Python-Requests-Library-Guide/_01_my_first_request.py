import requests

response = requests.get('https://api.github.com')

# 1xx Informational response
# 2xx Success
# 3xx Redirection
# 4xx Client errors
# 5xx Server errors
print(response)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

# requests goes one step further in simplifying this process for you. 
# If you use a Response instance in a conditional expression, 
# it will evaluate to True if the status code was between 200 and 400, 
# and False otherwise.


# https://realpython.com/operator-function-overloading/#making-your-objects-truthy-or-falsey-using-boolif response:
    print('Success!')
else:
    print('An error has occurred.')
