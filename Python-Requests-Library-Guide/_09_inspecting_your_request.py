"""

When you make a request, the requests library prepares the request before actually sending it to the destination server. 
Request preparation includes things like validating headers and serializing JSON content.

You can view the PreparedRequest by accessing .request:

"""

import requests
response = requests.post('https://httpbin.org/post', json={'key':'value'})

print(response.request.headers['Content-Type'])

print(response.request.url)

print(response.request.body)

