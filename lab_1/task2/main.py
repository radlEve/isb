import re

from constants import ENCODED_FILE, DECRYPTED_FILE, FOUND_KEY_FILE
from substitution import decrypt


def read_encoded_file() -> str:
    """
    Прочитать текстовый файл, указанный в константах, и вернуть в виде str
    :return: строка, содержащая весь текст файла
    """
    try:
        with open(ENCODED_FILE, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {ENCODED_FILE} не найден!")


def read_key_from_file(filepath: str) -> dict:
    """
    Считать ключ дешифровки из файла.
    Ожидаемый формат строки: "шифр_символ -> текст_символ"
    :param filepath: Путь к файлу с ключом.
    :return: Словарь {шифр_символ: текст_символ}.
    """
    key = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = re.split(r'\s*->\s*', line, maxsplit=1)

                if len(parts) == 2:
                    enc_char = parts[0]
                    dec_char = parts[1]

                    if dec_char == '':
                        dec_char = ' '

                    if enc_char == '':
                        enc_char = ' '

                    key[enc_char] = dec_char
    except Exception as e:
        raise Exception(f"Ошибка чтения файла ключа '{filepath}': {e}")

    return key


def write_results(decrypted_text: str) -> None:
    """
    Записать в отдельный файл (путь до которого указан в константах)
        расшифрованный текст
    :param decrypted_text: расшифрованный текст
    :return: None
    """
    try:
        with open(DECRYPTED_FILE, 'w', encoding='utf-8') as file:
            file.write(decrypted_text)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {ENCODED_FILE} не найден!")
    except Exception as e:
        raise Exception(f"Ошибка записи в {ENCODED_FILE}: {e}")



def main():
    try:
        encoded_text = read_encoded_file()

        found_key = read_key_from_file(FOUND_KEY_FILE)

        decrypted_text = decrypt(encoded_text, found_key)

        write_results(decrypted_text)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()