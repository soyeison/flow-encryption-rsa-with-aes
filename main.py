from aes import generate_key_ciphertext, decrypt_message
from rsa import encryp_message_using_public_pem, decrypt_message_using_private_pem

if __name__ == "__main__":
    # Cliente generar una clave AES aleatoria
    # Cliente cifra los datos con la clave AES aleatoria
    texto = "Este es el texto que se va a cifrar"
    print("Texto:", texto)

    cipher_key, cipher_text = generate_key_ciphertext(texto)

    # Cliente Utilizar la clave RSA publica del servidor para cifrar la clave AES
    # Cliente Utilizar la clave RSA publica del servidor para cifrar el mesaje de nuevo
    rsa_encrypted_aes_key = encryp_message_using_public_pem(cipher_key)
    rsa_encrypted_message = encryp_message_using_public_pem(cipher_text)
    print("Encrypted aes key with rsa:", rsa_encrypted_aes_key)
    print("Encrypted aes message with rsa:", rsa_encrypted_message)

    # ---------------------------------------------------------------------------

    # Servidor recibe los datos cifrados y la clave cifrada en rsa
    # Servidor utiliza la clave RSA privada para descifrar la clave AES y el mensaje.
    rsa_decrypted_aes_key = decrypt_message_using_private_pem(rsa_encrypted_aes_key)
    rsa_decrypted_message = decrypt_message_using_private_pem(rsa_encrypted_message)

    # El servidor utiliza la clave AES descifrada para descifrar los datos
    message = decrypt_message(rsa_decrypted_aes_key, rsa_decrypted_message)
    print("Message:", message)
