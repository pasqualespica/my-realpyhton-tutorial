

import requests

# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# You can pass params to get() in the form of a dictionary, as you have just done, or as a list of tuples:

# >> > requests.get(
#     ...     'https://api.github.com/search/repositories',
#     ...     params=[('q', 'requests+language:python')],
#     ...)

# You can even pass the values as bytes:

# >> > requests.get(
#     ...     'https://api.github.com/search/repositories',
#     ...     params=b'q=requests+language:python',
#     ...)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

# for k,v in json_response.items():
#     print(k, type(v))
#     # a = input("Dajee")
# for repo in json_response["items"]:
#     print(repo)
#     input()
