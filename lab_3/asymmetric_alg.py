from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding


class AsymmetricCipher:
    """
    Класс для асимметричного шифрования с использованием алгоритма RSA
    """

    @staticmethod
    def encrypt(original_data: bytes, public_key) -> bytes:
        """
        Шифрует данные с использованием открытого ключа
        :param original_data: Данные для шифрования в виде байтовой строки
        :param public_key: Открытый ключ RSA для шифрования
        :return: Зашифрованные данные
        """
        return public_key.encrypt(original_data,
                                  padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                               label=None))

    @staticmethod
    def decrypt(encrypted_data: bytes, private_key) -> bytes:
        """
        Дешифрует данные с использованием закрытого ключа
        :param encrypted_data: Зашифрованные данные для дешифрования
        :param private_key: Закрытый ключ RSA для дешифрования
        :return: Расшифрованные исходные данные
        """
        return private_key.decrypt(encrypted_data,
                                   padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                                label=None))
