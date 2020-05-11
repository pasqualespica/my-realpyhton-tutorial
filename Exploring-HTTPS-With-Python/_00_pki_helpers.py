# pki_helpers.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from datetime import datetime, timedelta
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes



"""

- The private key is your private color from the examples.
- The public key is the combined color that you shared.

The private key is something you always keep private, 
while the public key can be shared with anyone. 
These concepts map directly to the real world of Python HTTPS applications. 
Now that the server and the client have a shared secret, you can use your old pal symmetric encryption to encrypt all further messages!

Note: Public-key cryptography also relies on some math to do color mixing. The Wikipedia page for the Diffie-Hellman key exchange has a good explanation, but an in-depth explanation is outside the scope of this tutorial.

When you’re communicating over a secure website, like this one, your browser and the server set up a secure communication using these same principles:

1. Your browser requests information from the server.
2. Your browser and the server exchange public keys.
3. Your browser and the server generate a shared private key.
Your browser and the server encrypt and decrypt messages using this shared key through symmetric encryptio

"""


"""
The TTP scenario is how certificates are handled in practice. The process goes something like this:

1) Create a Certificate Signing Request (CSR): 
    This is like filling out the information for your visa.

2) Send the CSR to a Trusted Third Party (TTP): 
    This is like sending your information into a visa application office.

3) Verify your information: 
    Somehow, the TTP needs to verify the information you provided. As an example, see how Amazon validates ownership.

4) Generate a Public Key: 
    The TTP signs your CSR. This is equivalent to the TTP signing your visa.

5) Issue the verified Public Key: 
    This is equivalent to you receiving your visa in the mail.

"""
# ===============================
# 1) you’ll need to generate a private key as CA
# ===============================
def generate_private_key(filename: str, passphrase: str):
    """
        generate_private_key() generates a private key using RSA. Here’s a breakdown of the code:
        https://en.wikipedia.org/wiki/RSA_(cryptosystem)
    """
    private_key = rsa.generate_private_key(
        # https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#cryptography.hazmat.primitives.asymmetric.rsa.generate_private_key
        public_exponent=65537, key_size=2048, backend=default_backend()
    )

    utf8_pass = passphrase.encode("utf-8")
    algorithm = serialization.BestAvailableEncryption(utf8_pass)

    with open(filename, "wb") as keyfile:
        keyfile.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=algorithm,
            )
        )

    return private_key


# ===============================
# 2) The next step in becoming your own CA is to generate a self-signed public key. 
# You can bypass the certificate signing request (CSR) and immediately build a public key.
# ===============================
def generate_public_key(private_key, filename, **kwargs):
    subject = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, kwargs["country"]),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, kwargs["state"]),
            x509.NameAttribute(NameOID.LOCALITY_NAME, kwargs["locality"]),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, kwargs["org"]),
            x509.NameAttribute(NameOID.COMMON_NAME, kwargs["hostname"]),
        ]
    )

    # Because this is self signed, the issuer is always the subject
    issuer = subject

    # This certificate is valid from now until 30 days
    valid_from = datetime.utcnow()
    valid_to = valid_from + timedelta(days=30)

    # Used to build the certificate
    builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(valid_from)
        .not_valid_after(valid_to)
    )

    # Sign the certificate with the private key
    public_key = builder.sign(
        private_key, hashes.SHA256(), default_backend()
    )

    with open(filename, "wb") as certfile:
        certfile.write(public_key.public_bytes(serialization.Encoding.PEM))

    return public_key


# ===============================
# 3) Trusting Your Server
# The first step to your server becoming trusted is for you to generate a Certificate Signing Request(CSR). 
# In the real world, the CSR would be sent to an actual Certificate Authority like 
# - Verisign or
# - Let’s Encrypt. 
# In this example, you’ll use the CA you just created.
# Paste the code for generating a CSR into the pki_helpers.py file from above:
# ===============================
def generate_csr(private_key, filename, **kwargs):
    subject = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, kwargs["country"]),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, kwargs["state"]),
            x509.NameAttribute(NameOID.LOCALITY_NAME, kwargs["locality"]),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, kwargs["org"]),
            x509.NameAttribute(NameOID.COMMON_NAME, kwargs["hostname"]),
        ]
    )

    # Generate any alternative dns names
    alt_names = []
    for name in kwargs.get("alt_names", []):
        alt_names.append(x509.DNSName(name))
    san = x509.SubjectAlternativeName(alt_names)

    builder = (
        x509.CertificateSigningRequestBuilder()
        .subject_name(subject)
        .add_extension(san, critical=False)
    )

    csr = builder.sign(private_key, hashes.SHA256(), default_backend())

    with open(filename, "wb") as csrfile:
        csrfile.write(csr.public_bytes(serialization.Encoding.PEM))

    return csr

# ===============================
# 4) sign_csr
# With these two documents in hand, server-csr.pem  server-private-key.pem 
# you can now begin the process of signing your keys. Typically, 
# lots of verification would happen in this step. In the real world, 
# the CA would make sure that you owned my-site.com and ask you to prove it in various ways.
def sign_csr(csr, ca_public_key, ca_private_key, new_filename):
    valid_from = datetime.utcnow()
    valid_until = valid_from + timedelta(days=30)

    builder = (
        x509.CertificateBuilder()
        .subject_name(csr.subject)
        .issuer_name(ca_public_key.subject)
        .public_key(csr.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(valid_from)
        .not_valid_after(valid_until)
    )

    for extension in csr.extensions:
        # builder = builder.add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        builder = builder.add_extension(extension.value, extension.critical)

    public_key = builder.sign(
        private_key=ca_private_key,
        algorithm=hashes.SHA256(),
        backend=default_backend(),
    )

    with open(new_filename, "wb") as keyfile:
        keyfile.write(public_key.public_bytes(serialization.Encoding.PEM))
