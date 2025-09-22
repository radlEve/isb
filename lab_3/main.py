import argparse

from symmetric_alg import SymmetricCipher
from asymmetric_alg import AsymmetricCipher
from key_generation import KeyGeneration
from files_management import (
    read_json, serialize_private_key, serialize_public_key,
    deserialize_private_key,
    save_bytes_to_txt, load_bytes_from_txt
)


def generate_keys(config):
    print("Режим генерации ключей запущен")

    symmetric_key = KeyGeneration.generate_sym_key()
    print('Симметричный ключ сгенерирован')

    private_key, public_key = KeyGeneration.generate_asym_keys()
    print('Ключи ассиметричного алгоритма сгенерированы')

    serialize_private_key(private_key, config['secret_key'])
    serialize_public_key(public_key, config['public_key'])
    print("Приватный и публичный ключи сохранены")

    encrypted_symmetric_key = AsymmetricCipher.encrypt(symmetric_key, public_key)
    save_bytes_to_txt(encrypted_symmetric_key, config['symmetric_key'])
    print("Зашифрованный симметричный ключ сохранен")

    print('Успех! Генерация ключей завершена')


def encrypt_data(config):
    print("Режим шифрования данных запущен")

    private_key = deserialize_private_key(config['secret_key'])
    encrypted_symmetric_key = load_bytes_from_txt(config['symmetric_key'])
    symmetric_key = AsymmetricCipher.decrypt(encrypted_symmetric_key, private_key)
    print("Симметричный ключ расшифрован")

    with open(config['initial_file'], 'rb') as file:
        original_data = file.read()

    encrypted_data = SymmetricCipher.encrypt(original_data, symmetric_key)

    with open(config['encrypted_file'], 'wb') as file:
        file.write(encrypted_data)

    print("Файл зашифрован и сохранен")

    print("Успех! Шифрование завершено")


def decrypt_data(config):
    print("Режим дешифрования данных")

    private_key = deserialize_private_key(config['secret_key'])
    encrypted_symmetric_key = load_bytes_from_txt(config['symmetric_key'])
    symmetric_key = AsymmetricCipher.decrypt(encrypted_symmetric_key, private_key)
    print("Симметричный ключ расшифрован")

    with open(config['encrypted_file'], 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = SymmetricCipher.decrypt(encrypted_data, symmetric_key)

    with open(config['decrypted_file'], 'wb') as file:
        file.write(decrypted_data)

    print(f"Файл расшифрован и сохранен")

    print("Успех! Расшифрование завершено")


def main():
    parser = argparse.ArgumentParser(description='Гибридная криптосистема (RSA + IDEA)')

    group = parser.add_mutually_exclusive_group(required=True) # взаимоисключающие аргументы
    group.add_argument('-gen', '--generation', action='store_true',
                       help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', action='store_true',
                       help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', action='store_true',
                       help='Запускает режим дешифрования')

    parser.add_argument('-c', '--config', default='settings.json',
                        help='Путь к файлу конфигурации (по умолчанию: settings.json)')

    args = parser.parse_args()

    try:
        config = read_json(args.config)

        if args.encryption or args.decryption:
            required_files = ['initial_file', 'encrypted_file', 'decrypted_file',
                              'symmetric_key', 'secret_key', 'public_key']
            for key in required_files:
                if key not in config:
                    raise ValueError(f"Отсутствует обязательный параметр в конфиге: {key}")

        if args.generation:
            generate_keys(config)
        elif args.encryption:
            encrypt_data(config)
        elif args.decryption:
            decrypt_data(config)

    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    main()