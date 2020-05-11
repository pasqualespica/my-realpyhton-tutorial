# symmetric_client.py
import os
import requests
from cryptography.fernet import Fernet

# SECRET_KEY = os.environb[b"SECRET_KEY"]
SECRET_KEY = b"SwWRtuyI-xeIznp0BCLHdWVFx8WeuMd_Vdkvp0ljMBE ="
my_cipher = Fernet(SECRET_KEY)


def get_secret_message():
    response = requests.get("http://127.0.0.1:5000")

    decrypted_message = my_cipher.decrypt(response.content)
    print(f"The codeword is: {decrypted_message}")


if __name__ == "__main__":
    get_secret_message()
