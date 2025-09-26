import argparse

from files_management import FilesManagement
from scenarios import Scripts


def main():
    parser = argparse.ArgumentParser(description='Гибридная криптосистема (RSA + IDEA)')

    group = parser.add_mutually_exclusive_group(required=True)  # взаимоисключающие аргументы
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
        config = FilesManagement.read_json(args.config)

        if args.encryption or args.decryption:
            required_files = ['initial_file', 'encrypted_file', 'decrypted_file',
                              'symmetric_key', 'secret_key', 'public_key']
            for key in required_files:
                if key not in config:
                    raise ValueError(f"Отсутствует обязательный параметр в конфиге: {key}")

        if args.generation:
            Scripts.generate_keys(config)
        elif args.encryption:
            Scripts.encrypt_data(config)
        elif args.decryption:
            Scripts.decrypt_data(config)

    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    main()
