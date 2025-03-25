from constants import INPUT_FILE, ENCRYPTED_FILE, KEY_FILE
from vigenere import encrypt


def read_file(filename: str) -> str:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {filename} не найден!")


def write_file(filename: str, content: str) -> None:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {filename} не найден!")
    except Exception as e:
        raise Exception(f"Ошибка записи в {filename}: {e}")


def main():
    try:
        original_text = read_file(INPUT_FILE)

        key = read_file(KEY_FILE)

        encrypted_text = encrypt(original_text, key)

        write_file(ENCRYPTED_FILE, encrypted_text)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()