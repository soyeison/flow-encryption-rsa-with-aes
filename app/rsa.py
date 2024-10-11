import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from getpass import getpass


def generate_pem_keys():
    # Generate a new RSA key
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

    # Serializar la llave privada en formato PEM
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )

    # Llevarme el contenido serializado de la public key a un archivo
    with open("private_key.pem", "wb") as f:
        f.write(private_pem)

    # -------------------------------------------------------------

    # Get de public key
    public_key = private_key.public_key()

    # Serialize the public key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    # Llevarme el contenido serializado de la public key a un archivo
    with open("public_key.pem", "wb") as f:
        f.write(public_pem)


def encryp_message_using_public_pem(message: bytes):
    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(f.read())

        ciphertext = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

    return base64.b64encode(ciphertext).decode("utf-8")


def decrypt_message_using_private_pem(message: str):
    message_bytes = base64.b64decode(message)
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(f.read(), password=None)

        decrypted_message = private_key.decrypt(
            message_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        return decrypted_message
