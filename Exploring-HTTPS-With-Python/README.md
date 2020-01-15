


# Useful links
<!-- Following link is the mai article resource  -->
https://realpython.com/python-https/

https://en.wikipedia.org/wiki/Transmission_Control_Protocol

https://www.restapitutorial.com/

https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview


# Environment steps 
1. pip install -r requirements.txt

# HowTo... and Tip&Tricks 

## Install uwsgi
Although `uwsgi` shall install via "pip" on MacOs I had some issues, and to solve it I preferred install it via `brew`

```bash
brew install uwsgi
```

## Run uwsgi server and client app ( on HTTP )

I don't use port 5683 becauce it associated to Constrained Application Protocol (CoAP) into WireShark 

![alt text](img/coAP.png)

now to run server type this on a `shell` terminal

```bash
uwsgi --http-socket 127.0.0.1:5985 --mount /=server:app
```
and to launch a client via `browser` type

```bash
http://localhost:5985/
```

or via shell by `curl` type 

```bash
curl localhost:5985/
```

## Using Cryptography
https://en.wikipedia.org/wiki/Symmetric-key_algorithm

The previous exmaple shows through  Wireshark the plain content-text, now 
try using cryptography 

to generate a random and secure key type from python-shell

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
key
```

and using it as follow :

```python
my_cipher = Fernet(key)
ciphertext = my_cipher.encrypt(b"fluffy tail")
ciphertext
```

noe running server and client with symmetric chiper

### server-side
```bash
uwsgi --http-socket 127.0.0.1:5985 \
    --env SECRET_KEY="8jtTR9QcD-k3RO9Pcd5ePgmTu_itJQt9WKQPzqjrcoM=" \
    --mount /=symmetric_server:app
```
### client-side
```bash
SECRET_KEY="8jtTR9QcD-k3RO9Pcd5ePgmTu_itJQt9WKQPzqjrcoM=" python symmetric_client.py
```
Awesome! 

Your data is safe! But wait a minute—you never had to know anything about a key 
when you were using Python HTTPS applications before. 

That’s because HTTPS doesn’t use symmetric encryption exclusively. 
As it turns out, sharing secrets is a hard problem.

## How Are Keys Shared?

What you need is for two parties that have never communicated to have a shared secret. Sounds impossible, right? Luckily, three guys by the names of Ralph Merkle, Whitfield Diffie, and Martin Hellman have your back. They helped demonstrate that public-key cryptography, otherwise known as asymmetric encryption, was possible.

https://en.wikipedia.org/wiki/Public-key_cryptography

**Asymmetric encryption** allows for two users who have never communicated before to share a common secret. One of the easiest ways to understand the fundamentals is to use a color analogy. Imagine you have the following scenario: