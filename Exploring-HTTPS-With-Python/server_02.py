# server.py
from flask import Flask
import ssl

SECRET_MESSAGE = "fluffy tail"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return SECRET_MESSAGE

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain('server-public-key.pem', 'server-private-key.pem')
    app.run('127.0.0.1', 5000, ssl_context=context)

