import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def read_json(js_file: str) -> dict:
    try:
        with open(js_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        raise Exception(f"Error: {e}")


def serialize_private_key(private_key, pem_path):
    try:
        with open(pem_path, 'wb') as file:
            file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                 format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                 encryption_algorithm=serialization.NoEncryption()))
    except Exception as e:
        raise Exception(f'Error: {e}')


def serialize_public_key(public_key, pem_path):
    try:
        with open(pem_path, 'wb') as file:
            file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                               format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as e:
        raise Exception(f'Error: {e}')


def deserialize_private_key(pem_path):
    try:
        with open(pem_path, 'rb') as file:
            private_bytes = file.read()
        return load_pem_private_key(private_bytes, password=None)
    except Exception as e:
        raise Exception(f'Error: {e}')


def deserialize_public_key(pem_path):
    try:
        with open(pem_path, 'rb') as file:
            public_bytes = file.read()
        return load_pem_public_key(public_bytes)
    except Exception as e:
        raise Exception(f'Error: {e}')


def save_bytes_to_txt(data: bytes, file_path: str):
    with open(file_path, 'wb') as file:
        file.write(data)


def load_bytes_from_txt(file_path: str):
    with open(file_path, 'rb') as file:
        return file.read()

