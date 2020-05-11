# symmetric_server.py
import os
from flask import Flask
from cryptography.fernet import Fernet


# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# key

# SECRET_KEY = os.environb[b"SECRET_KEY"]
SECRET_KEY = b"SwWRtuyI-xeIznp0BCLHdWVFx8WeuMd_Vdkvp0ljMBE ="
SECRET_MESSAGE = b"fluffy tail"
app = Flask(__name__)

my_cipher = Fernet(SECRET_KEY)

@app.route("/")
def get_secret_message():
    return my_cipher.encrypt(SECRET_MESSAGE)
