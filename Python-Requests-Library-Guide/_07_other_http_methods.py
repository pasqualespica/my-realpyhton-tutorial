import requests

# requests.post('https://httpbin.org/post', data={'key': 'value'})
# requests.put('https://httpbin.org/put', data={'key': 'value'})
# requests.delete('https://httpbin.org/delete')
# requests.head('https://httpbin.org/get')
# requests.patch('https://httpbin.org/patch', data={'key': 'value'})
# requests.options('https://httpbin.org/get')

"""
Each function call makes a request to the httpbin service using the corresponding HTTP method. 
For each method, you can inspect their responses in the same way you did before:
"""

response = requests.head('https://httpbin.org/get')
print(response.headers['Content-Type'])


response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])


"""
- Headers
- response bodies
- status codes
- and more are returned in the Response for each method. 

Next you’ll take a closer look at the POST, PUT, and PATCH methods and learn how they differ from the other request types.


"""
