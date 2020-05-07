import requests

"""

The Message Body
According to the HTTP specification, POST, PUT, and the less common PATCH requests 
pass their data through the message body rather than through parameters in the query string. 
Using requests, you’ll pass the payload to the corresponding function’s data parameter.

data takes a dictionary, a list of tuples, bytes, or a file-like object. 
You’ll want to adapt the data you send in the body of your request to the specific needs of the service you’re interacting with.

"""

# For example, if your request’s content type is application/x-www-form-urlencoded, 
# you can send the form data as a dictionary:

r = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(r)

# You can also send that same data as a list of tuples:

r = requests.post('https://httpbin.org/post', data=[('key', 'value11')])
print(r)


"""

If, however, you need to send JSON data, you can use the json parameter. 
When you pass JSON data via json, requests will serialize your data and add the correct Content-Type header for you.

httpbin.org is a great resource created by the author of requests, Kenneth Reitz. 
It’s a service that accepts test requests and responds with data about the requests. 
For instance, you can use it to inspect a basic POST request:

"""

response = requests.post('https://httpbin.org/post', json={'key': 'value11'})
json_response = response.json()
print(json_response['headers']['Content-Length'])
print(json_response['data'])

print(json_response['headers']['Content-Type'])
