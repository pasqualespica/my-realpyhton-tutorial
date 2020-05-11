
CIPHER = {"a": "z", "A": "Z", "b": "a"}  # And so on


def encrypt(plaintext: str):
    return "".join(CIPHER.get(letter, letter) for letter in plaintext)


DECIPHER = {v: k for k, v in CIPHER.items()}


def decrypt(ciphertext: str):
    return "".join(DECIPHER.get(letter, letter) for letter in ciphertext)


SECRET_PWD = "PasqualeSpica"
print(f"SECRET_PWD {SECRET_PWD}")

encrypt_pwd = encrypt(SECRET_PWD)
print(f"encrypt {encrypt_pwd}")

decrypt_pwd = decrypt(encrypt_pwd)
print(f"decrypt {decrypt_pwd}")


