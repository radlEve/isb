import os
from cryptography.hazmat.primitives.asymmetric import rsa


class KeyGeneration:
    @staticmethod
    def generate_sym_key() -> bytes:
        return os.urandom(16)

    @staticmethod
    def generate_asym_keys() -> tuple:
        key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        return key, key.public_key()