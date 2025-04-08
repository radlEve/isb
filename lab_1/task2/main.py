from constants import ENCODED_FILE, DECRYPTED_FILE, FOUND_KEY_FILE
from lab_1.task2.constants import CHAR_REPLACEMENTS
from substitution import get_frequency_key, decrypt


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


def apply_manual_corrections(key: dict, replacements: list[tuple[str, str]]) -> dict:
    """
    Применить ручные изменения для ключа,
    поочередно меняя местами по 2 буквы из алфавита
    :param key: исходный ключ (словарь {шифр_буква: обычная_буква})
    :param replacements: список букв,
        которые необходимо поменять местами в заданном порядке
    :return: итоговый ключ
    """
    new_key = key.copy()

    for char1, char2 in replacements:
        key_upd = {}
        for cipher_char, plain_char in new_key.items():
            if plain_char == char1:
                key_upd[cipher_char] = char2
            elif plain_char == char2:
                key_upd[cipher_char] = char1

        new_key.update(key_upd)

    return new_key


def main():
    try:
        encoded_text = read_encoded_file()

        found_key = get_frequency_key(encoded_text)

        found_key = apply_manual_corrections(found_key, CHAR_REPLACEMENTS)

        decrypted_text = decrypt(encoded_text, found_key)

        write_results(decrypted_text, found_key)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()