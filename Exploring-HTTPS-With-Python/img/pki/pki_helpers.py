# pki_helpers.py
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from datetime import datetime, timedelta
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes


# The TTP scenario is how certificates are handled in practice. 
#       The process goes something like this:


#   1.  Create a Certificate Signing Request(CSR): 
#       This is like filling out the information for your visa.

#   2.  Send the CSR to a Trusted Third Party(TTP): 
#       This is like sending your information into a visa application office.

#   3.  Verify your information: 
#       Somehow, the TTP needs to verify the information you provided. As an example, see how Amazon validates ownership.

#   4.  Generate a Public Key: 
#       The TTP signs your CSR. This is equivalent to the TTP signing your visa.

#   5.  Issue the verified Public Key: 
#       This is equivalent to you receiving your visa in the mail.

#   Note that the CSR is tied cryptographically to your private key. 
#   As such, all three pieces of information—public key, private key, and 
#   certificate authority—are related in one way or another. 
#   This creates what is known as a chain of trust, so you now have a valid 
#   certificate that can be used to verify your identity.



def generate_private_key(filename: str, passphrase: str):
    """
    For starters, you’ll need to generate a private key
    """
    private_key = rsa.generate_private_key(
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


def generate_public_key(private_key, filename, **kwargs):
    """
    generate a self-signed public key
    """

    subject = x509.Name(
        [
            x509.NameAttribute(NameOID.COUNTRY_NAME, kwargs["country"]),
            x509.NameAttribute(
                NameOID.STATE_OR_PROVINCE_NAME, kwargs["state"]
            ),
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
