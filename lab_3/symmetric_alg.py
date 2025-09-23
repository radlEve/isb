import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class SymmetricCipher:
    """
    Класс для симметричного шифрования с использованием алгоритма IDEA
    """

    @staticmethod
    def encrypt(original_data: bytes, key: bytes) -> bytes:
        """
        Шифрует данные с использованием алгоритма IDEA в режиме CBC
        :param original_data: Исходные данные для шифрования (в виде байтов)
        :param key: Ключ шифрования длиной 128 бит
        :return: Зашифрованные данные + вектор инициализации
        """
        if len(key) != 16:
            raise ValueError("Ключ должен быть длиной 128 бит")

        padder = padding.ANSIX923(64).padder()
        padded_text = padder.update(original_data) + padder.finalize()

        iv = os.urandom(8)
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        return encryptor.update(padded_text) + encryptor.finalize() + iv

    @staticmethod
    def decrypt(encrypted_data: bytes, key: bytes) -> bytes:
        """
        Дешифрует данные, зашифрованные методом encrypt
        :param encrypted_data: Зашифрованные данные с iv в конце
        :param key: Ключ шифрования длиной 128 бит
        :return: Ключ шифрования длиной 128 бит
        """
        if len(key) != 16:
            raise ValueError("Ключ должен быть длиной 128 бит")

        iv = encrypted_data[-8:]
        cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        c_text = encrypted_data[:-8]
        dc_text = decryptor.update(c_text) + decryptor.finalize()

        unpadder = padding.ANSIX923(64).unpadder()
        unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        return unpadded_dc_text
