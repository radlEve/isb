import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class SymmetricCipher:
    @staticmethod
    def encrypt(original_data: bytes, key: bytes):
        padder = padding.ANSIX923(64).padder()
        padded_text = padder.update(original_data) + padder.finalize()

        iv = os.urandom(8)
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        return  encryptor.update(padded_text) + encryptor.finalize() + iv

    @staticmethod
    def decrypt(encrypted_data: bytes, key: bytes):
        iv = encrypted_data[-8:]
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        c_text = encrypted_data[:-8]
        dc_text = decryptor.update(c_text) + decryptor.finalize()

        unpadder = padding.ANSIX923(64).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        return unpadded_dc_text

