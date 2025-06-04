from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = b'0123456789abcdef0123456789abcdef'
iv = os.urandom(16)


def encrypt_message(message):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padded = message + ' ' * (16 - len(message) % 16)
    encrypted = encryptor.update(padded.encode()) + encryptor.finalize()
    return iv + encrypted

def decrypt_message(encrypted):
    iv_local = encrypted[:16]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv_local), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted[16:]) + decryptor.finalize()
    return decrypted.decode().rstrip()