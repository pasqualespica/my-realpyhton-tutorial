# Headers
# The response headers can give you useful information, such as the content
# type of the response payload and a time limit on how long to cache the response. 
# To view these headers, access 
# 
# .headers

import requests

response = requests.get('https://api.github.com')

# <class 'requests.structures.CaseInsensitiveDict'>
print(response.headers)
print()
print(response.headers['Content-Type'])

