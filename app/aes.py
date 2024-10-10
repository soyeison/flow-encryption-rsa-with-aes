import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

plain_text = "Este es un mensaje"  # El mensaje tiene que ser de 16 bytes por lo que se usa padding para rellenar

# Generar una clave AES aleatoria (256 bits = 32 bytes)
""" aes_key = os.urandom(32)

print("Aes key:", aes_key)

print("Key en base 64 utf8:", base64.b64encode(aes_key).decode("utf-8"))

# Crear e cifrado AES en modo ECB
cipher = Cipher(algorithms.AES(aes_key), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()

# Aplicar padding PKCS7 (bloques de 128 bits = 16 bytes)
padder = padding.PKCS7(128).padder()
padded_plaintext = padder.update(plain_text) + padder.finalize()

# Cifrar el mensaje con padding
ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

print(f"Texto cifrado: {ciphertext}")

ciphertext_base64 = base64.b64encode(ciphertext).decode("utf-8")

print(f"Texto cifrado en base 64: {ciphertext_base64}") """


def generate_key_ciphertext(message: str):
    message_encoded = message.encode()
    aes_key = os.urandom(32)
    aes_key_base64 = base64.b64encode(aes_key).decode("utf-8")

    cipher = Cipher(algorithms.AES(aes_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(message_encoded) + padder.finalize()

    # Cifrar el mensaje con padding
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    ciphertext_base64 = base64.b64encode(ciphertext).decode("utf-8")

    return aes_key_base64, ciphertext_base64


key, ciphertext = generate_key_ciphertext(plain_text)

print("Key:", key)
print("ciphertext:", ciphertext)
