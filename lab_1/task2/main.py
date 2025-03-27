from constants import ENCODED_FILE, DECRYPTED_FILE, FOUND_KEY_FILE
from lab_1.task2.constants import CHAR_REPLACEMENTS
from substitution import decrypt


def read_encoded_file() -> str:
    try:
        with open(ENCODED_FILE, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {ENCODED_FILE} не найден!")

def write_results(decrypted_text: str, key: dict) -> None:
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


def apply_manual_corrections(text: str, replacements: list[tuple[str, str]]):
    results = text
    for char1, char2 in replacements:
        result = result.replace(char1, '\0').replace(char2, char1).replace('\0', char2)
    return result



def main():
    try:
        encoded_text = read_encoded_file()

        decrypted_text, found_key = decrypt(encoded_text)

        apply_manual_corrections(decrypted_text, CHAR_REPLACEMENTS)

        write_results(decrypted_text, found_key)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()