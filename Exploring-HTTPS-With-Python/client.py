# client.py
import os
import requests

SECRET_URL="https://127.0.0.1:5000/"
def get_secret_message():
    # url = os.environ["SECRET_URL"]
    url = SECRET_URL
    response = requests.get(url)
    print(f"The secret message is: {response.text}")


if __name__ == "__main__":
    get_secret_message()
