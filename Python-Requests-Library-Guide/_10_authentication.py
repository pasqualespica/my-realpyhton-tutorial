import requests
from getpass import getpass

resp = requests.get('https://api.github.com/user', auth=('pasqualespica', getpass()))

print(resp.json())


resp = requests.get('https://api.github.com/user')

# https://developer.mozilla.org/it/docs/Web/HTTP/Status
print(resp) # 401 Unauthorized


"""
https://en.wikipedia.org/wiki/Basic_access_authentication

When you pass your username and password in a tuple to the auth parameter, requests is applying the credentials using HTTP’s Basic access authentication scheme under the hood.

Therefore, you could make the same request by passing explicit Basic authentication credentials using HTTPBasicAuth:

"""

from requests.auth import HTTPBasicAuth
requests.get( 'https://api.github.com/user', auth=HTTPBasicAuth('username', getpass() ))
