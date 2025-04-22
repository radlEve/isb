from constants import ENCODED_FILE, DECRYPTED_FILE, FOUND_KEY_FILE
from lab_1.task2.constants import FINAL_KEY
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

def write_results(decrypted_text: str, key: dict) -> None:
    """
    Записать в отдельные файлы (пути до которых указаны в константах)
        расшифрованный текст и ключ в виде "*char_before* -> *char_after*"
    :param decrypted_text: расшифрованный текст
    :param key: ключ для расшифровки исходного текста
    :return: None
    """
    try:
        with open(DECRYPTED_FILE, 'w', encoding='utf-8') as file:
            file.write(decrypted_text)
        with open(FOUND_KEY_FILE, 'w', encoding='utf-8') as file:
            for enc_char, dec_char in key.items():
                file.write(f"{enc_char} -> {dec_char}\n")
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {ENCODED_FILE} не найден!")
    except Exception as e:
        raise Exception(f"Ошибка записи в {ENCODED_FILE}: {e}")



def main():
    try:
        encoded_text = read_encoded_file()

        decrypted_text = decrypt(encoded_text, FINAL_KEY)

        write_results(decrypted_text, FINAL_KEY)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()