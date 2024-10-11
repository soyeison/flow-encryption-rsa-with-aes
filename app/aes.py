import base64
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


def generate_key_ciphertext(message: str):
    message_encoded = message.encode()
    aes_key = os.urandom(32)

    cipher = Cipher(algorithms.AES(aes_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(message_encoded) + padder.finalize()

    # Cifrar el mensaje con padding
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return aes_key, ciphertext


def decrypt_message(key: bytes, ciphermessage: bytes):
    decryptor = Cipher(
        algorithms.AES(key), modes.ECB(), backend=default_backend()
    ).decryptor()

    decrypted_message = decryptor.update(ciphermessage) + decryptor.finalize()

    return decrypted_message.decode("utf-8")
