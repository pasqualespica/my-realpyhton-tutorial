from getpass import getpass
import requests
# The Session Object
# Until now, you’ve been dealing with high level requests APIs such as get() and post(). These functions are abstractions of what’s going on when you make your requests. They hide implementation details such as how connections are managed so that you don’t have to worry about them.

# Underneath those abstractions is a class called Session. If you need to fine-tune your control over how requests are being made or improve the performance of your requests, you may need to use a Session instance directly.

# Sessions are used to persist parameters across requests. For example, if you want to use the same authentication across multiple requests, you could use a session:

    # By using a context manager, you can ensure the resources used by
    # the session will be released after use
with requests.Session() as session:
    session.auth = ('username', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')

# You can inspect the response just like you did before
print(response.headers)
print(response.json())
# Each time you make a request with session, once it has been initialized with authentication credentials, the credentials will be persisted.

# The primary performance optimization of sessions comes in the form of persistent connections. When your app makes a connection to a server using a Session, it keeps that connection around in a connection pool. When your app wants to connect to the same server again, it will reuse a connection from the pool rather than establishing a new one.
