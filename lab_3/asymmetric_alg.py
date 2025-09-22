from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.asymmetric import padding


class AsymmetricCipher:
    @staticmethod
    def encrypt(original_data: bytes, public_key) -> bytes:
        return public_key.encrypt(original_data,
                                  padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                               label=None))

    @staticmethod
    def decrypt(encrypted_data: bytes, private_key):
        return private_key.decrypt(encrypted_data,
                                   padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                                label=None))
