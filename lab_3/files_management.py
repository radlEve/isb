import json
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def read_json(js_file: str) -> dict:
    """
    Читает и парсит JSON-файл
    :param js_file: Путь к JSON-файлу для чтения
    :return: Словарь с данными из JSON-файла
    """
    try:
        with open(js_file, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        raise Exception(f"Error: {e}")


def serialize_private_key(private_key: RSAPrivateKey, pem_path: str) -> None:
    """
    Сериализует приватный ключ в PEM-формат и сохраняет в файл
    :param private_key: Приватный ключ для сериализации
    :param pem_path: Путь для сохранения PEM-файла
    :return: None
    """
    try:
        with open(pem_path, 'wb') as file:
            file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                 format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                 encryption_algorithm=serialization.NoEncryption()))
    except Exception as e:
        raise Exception(f'Error: {e}')


def serialize_public_key(public_key: RSAPublicKey, pem_path: str) -> None:
    """
    Сериализует публичный ключ в PEM-формат и сохраняет в файл
    :param public_key: Публичный ключ для сериализации
    :param pem_path: Путь для сохранения PEM-файла
    :return: None
    """
    try:
        with open(pem_path, 'wb') as file:
            file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                               format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as e:
        raise Exception(f'Error: {e}')


def deserialize_private_key(pem_path: str) -> RSAPrivateKey:
    """
    Загружает и десериализует приватный ключ из PEM-файла
    :param pem_path: Путь к PEM-файлу с приватным ключом
    :return: Десериализованный приватный ключ
    """
    try:
        with open(pem_path, 'rb') as file:
            private_bytes = file.read()
        return load_pem_private_key(private_bytes, password=None)
    except Exception as e:
        raise Exception(f'Error: {e}')


def deserialize_public_key(pem_path: str) -> RSAPublicKey:
    """
    Загружает и десериализует публичный ключ из PEM-файла
    :param pem_path: Путь к PEM-файлу с публичным ключом
    :return: Десериализованный публичный ключ
    """
    try:
        with open(pem_path, 'rb') as file:
            public_bytes = file.read()
        return load_pem_public_key(public_bytes)
    except Exception as e:
        raise Exception(f'Error: {e}')


def save_bytes_to_txt(data: bytes, file_path: str) -> None:
    """
    Сохраняет байтовые данные в бинарный файл
    :param data: Байтовые данные для сохранения
    :param file_path: Путь к файлу для сохранения
    :return: None
    """
    with open(file_path, 'wb') as file:
        file.write(data)


def load_bytes_from_txt(file_path: str) -> bytes:
    """
    Загружает байтовые данные из бинарного файла
    :param file_path: Путь к файлу для чтения
    :return: Байтовые данные из файла
    """
    with open(file_path, 'rb') as file:
        return file.read()
