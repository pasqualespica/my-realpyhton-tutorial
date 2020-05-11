from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(f"key {key}")


my_cipher = Fernet(key)
ciphertext = my_cipher.encrypt(b"fluffy tail")
print(f"ciphertext{ciphertext}")

plain_text = my_cipher.decrypt(ciphertext)
print(f"plain_text {plain_text}")

