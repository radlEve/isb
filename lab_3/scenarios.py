from symmetric_alg import SymmetricCipher
from asymmetric_alg import AsymmetricCipher
from key_generation import KeyGeneration
from files_management import FilesManagement


class Scripts:
    """
    Сценарии выполнения программы
    """

    @staticmethod
    def generate_keys(config: dict[str, str]) -> None:
        """
        Генерирует и сохраняет ключи для гибридной криптосистемы
        :param config: Словарь с путями для сохранения ключей и файлов
        :return: None
        """
        print("Режим генерации ключей запущен")

        symmetric_key = KeyGeneration.generate_sym_key()
        print('Симметричный ключ сгенерирован')

        private_key, public_key = KeyGeneration.generate_asym_keys()
        print('Ключи ассиметричного алгоритма сгенерированы')

        FilesManagement.serialize_private_key(private_key, config['secret_key'])
        FilesManagement.serialize_public_key(public_key, config['public_key'])
        print("Приватный и публичный ключи сохранены")

        encrypted_symmetric_key = AsymmetricCipher.encrypt(symmetric_key, public_key)
        FilesManagement.save_bytes_to_txt(encrypted_symmetric_key, config['symmetric_key'])
        print("Зашифрованный симметричный ключ сохранен")

        print('Успех! Генерация ключей завершена')

    @staticmethod
    def encrypt_data(config: dict[str, str]) -> None:
        """
        Шифрует файл с использованием гибридной криптосистемы
        :param config: Словарь с путями к файлам и ключам
        :return: None
        """
        print("Режим шифрования данных запущен")

        private_key = FilesManagement.deserialize_private_key(config['secret_key'])
        encrypted_symmetric_key = FilesManagement.load_bytes_from_txt(config['symmetric_key'])
        symmetric_key = AsymmetricCipher.decrypt(encrypted_symmetric_key, private_key)
        print("Симметричный ключ расшифрован")

        with open(config['initial_file'], 'rb') as file:
            original_data = file.read()

        encrypted_data = SymmetricCipher.encrypt(original_data, symmetric_key)

        with open(config['encrypted_file'], 'wb') as file:
            file.write(encrypted_data)

        print("Файл зашифрован и сохранен")

        print("Успех! Шифрование завершено")

    @staticmethod
    def decrypt_data(config: dict[str, str]) -> None:
        """
        Дешифрует файл, зашифрованный гибридной криптосистемой
        :param config: Словарь с путями к файлам и ключам
        :return: None
        """
        print("Режим дешифрования данных")

        private_key = FilesManagement.deserialize_private_key(config['secret_key'])
        encrypted_symmetric_key = FilesManagement.load_bytes_from_txt(config['symmetric_key'])
        symmetric_key = AsymmetricCipher.decrypt(encrypted_symmetric_key, private_key)
        print("Симметричный ключ расшифрован")

        with open(config['encrypted_file'], 'rb') as file:
            encrypted_data = file.read()

        decrypted_data = SymmetricCipher.decrypt(encrypted_data, symmetric_key)

        with open(config['decrypted_file'], 'wb') as file:
            file.write(decrypted_data)

        print(f"Файл расшифрован и сохранен")

        print("Успех! Расшифрование завершено")
