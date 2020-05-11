# client.py
import os
import requests

SECRET_URL="https://127.0.0.1:5000/"
def get_secret_message():

    # url = os.environ["SECRET_URL"]
    url = SECRET_URL

    response = requests.get("https://127.0.0.1:5000/", verify="server-public-key.pem")
#    response = requests.get("https://127.0.0.1:5000/", verify="ca-public-key.pem")

    print(f"The secret message is: {response.text}")


"""
or by bash
https://tech-habit.info/posts/https-cert-based-auth-with-flask-and-gunicorn/

curl --insecure https://127.0.0.1:5000/

"""

if __name__ == "__main__":
    get_secret_message()



