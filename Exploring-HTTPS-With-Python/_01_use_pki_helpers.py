from cryptography.hazmat.primitives import serialization
from getpass import getpass
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from _00_pki_helpers import generate_private_key, generate_public_key, generate_csr, sign_csr

print("STEP 1 - CA : public/private keys\n")
# 1 - CA : public/private keys
# `pas-ca` is PASSWORD for Certificate Authority
private_key = generate_private_key("ca-private-key.pem", "pas-ca")
print(f"private_key genetared : {private_key}\n")

# The next step in becoming your own CA is to generate a self-signed public key. 
# You can bypass the certificate signing request (CSR) and 
# immediately build a public key
print("and generate CA ca-public-key.pem \n")
generate_public_key(
    private_key,
    filename="ca-public-key.pem",
    country="US",
    state="Maryland",
    locality="Baltimore",
    org="My CA Company",
    hostname="my-ca.com",
)

print("STEP 2 - SERVER : generate private keys\n")
# 2 - SERVER : private keys
# `pas-svr` is PASSWORD for SERVER
server_private_key = generate_private_key(
    "server-private-key.pem", "pas-svr"
)

print("STEP 3 - SERVER : Certificate Signing Request (CSR) contains public key\n")
# 3 - SERVER : Certificate Signing Request (CSR)
generate_csr(
    server_private_key,
    filename="server-csr.pem",
    country="US",
    state="Maryland",
    locality="Baltimore",
    org="My Company",
    alt_names=["localhost","127.0.0.1"],
    hostname="my-site.com",
)


# 4 - Sign CSR by CA
print("STEP 4 - load CSR SERVER\n")
csr_file = open("server-csr.pem", "rb")
csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())
print(f"csr : {csr}\n")

print("load ca-public-key.pem\n")
ca_public_key_file = open("ca-public-key.pem", "rb")
ca_public_key = x509.load_pem_x509_certificate(
    ca_public_key_file.read(), default_backend()
)
print(f"ca_public_key : {ca_public_key}\n")

# Once again, you’ve created a ca_public_key object which can be used by sign_csr()

print("load ca-private-key.pem\n")
ca_private_key_file = open("ca-private-key.pem", "rb")
ca_private_key = serialization.load_pem_private_key(
    ca_private_key_file.read(),
    getpass("Insert Certificate Authority password tp SING CSR for server :").encode("utf-8"),
    default_backend(),
)
print(f"ca_private_key : {ca_private_key}\n")

sign_csr(csr, ca_public_key, ca_private_key, "server-public-key.pem")
print(f"generate  server-public-key.pem : {ca_private_key}\n")
