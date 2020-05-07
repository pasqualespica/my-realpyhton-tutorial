
import requests

response = requests.get('https://api.github.com')

# To see the response’s content in bytes, you use .content:

# print(">>> .content To see the response’s content in bytes >>>",
#       response.content, sep="\n")

# you will often want to convert them into a string using a character
#  encoding such as UTF-8. response will do that for you when you access .text:

# print(">>> .text To see such as UTF >>>",
#     response.text)

response.encoding = 'utf-8'  # Optional: requests infers this internally
print(response.text)

json_rsp = response.json()  # return a <class 'dict'>
print(json_rsp["current_user_url"])
