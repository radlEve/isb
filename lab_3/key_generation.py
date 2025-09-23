import os
from cryptography.hazmat.primitives.asymmetric import rsa


class KeyGeneration:
    """
    Класс для генерации ключей симметричного и асимметричного алгоритмов
    """

    @staticmethod
    def generate_sym_key(key_size: int = 16) -> bytes:
        """
        Генерирует симметричный ключ заданного размера
        :param key_size: Размер ключа в байтах (по умолчанию 16 для IDEA)
        :return: Случайный симметричный ключ заданного размера
        """
        return os.urandom(key_size)

    @staticmethod
    def generate_asym_keys() -> tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        """
        Генерирует пару асимметричных ключей RSA заданного размера
        :return: Кортеж из приватного и публичного ключей
        """
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        return key, key.public_key()
