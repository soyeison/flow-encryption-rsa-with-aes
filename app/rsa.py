from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from getpass import getpass

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

# -------------------------------------------------------------

# Mensaje que se va a encriptar
""" message = "Este es un mensaje encrytado"

# Encrypt message
ciphertext = public_key.encrypt(
    message.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
) """
