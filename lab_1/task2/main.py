from constants import ENCODED_FILE, DECRYPTED_FILE, FOUND_KEY_FILE
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


def swap_chars(text: str, char1: str, char2: str) -> str:
    result = []
    for char in text:
        if char == char1:
            result.append(char2)
        elif char == char2:
            result.append(char1)
        else:
            result.append(char)
    return ''.join(result)


def main():
    try:
        encoded_text = read_encoded_file()

        decrypted_text, found_key = decrypt(encoded_text)

        decrypted_text = swap_chars(decrypted_text, 'Р', 'К')
        decrypted_text = swap_chars(decrypted_text, 'С', 'А')
        decrypted_text = swap_chars(decrypted_text, 'Д', 'П')
        decrypted_text = swap_chars(decrypted_text, 'Ь', 'Ч')
        decrypted_text = swap_chars(decrypted_text, 'С', 'Т')
        decrypted_text = swap_chars(decrypted_text, 'Р', 'В')
        decrypted_text = swap_chars(decrypted_text, 'Л', 'М')
        decrypted_text = swap_chars(decrypted_text, 'Р', 'Я')
        decrypted_text = swap_chars(decrypted_text, 'Р', 'П')
        decrypted_text = swap_chars(decrypted_text, 'Р', 'Л')
        decrypted_text = swap_chars(decrypted_text, 'Г', 'Э')
        decrypted_text = swap_chars(decrypted_text, 'У', 'Й')
        decrypted_text = swap_chars(decrypted_text, 'З', 'Ь')
        decrypted_text = swap_chars(decrypted_text, 'Х', 'Ы')
        decrypted_text = swap_chars(decrypted_text, 'Ф', 'Г')
        decrypted_text = swap_chars(decrypted_text, 'Х', 'У')
        decrypted_text = swap_chars(decrypted_text, 'Х', 'Ц')
        decrypted_text = swap_chars(decrypted_text, 'Х', 'Б')
        decrypted_text = swap_chars(decrypted_text, 'Х', 'Щ')
        decrypted_text = swap_chars(decrypted_text, 'Ш', 'Ю')
        decrypted_text = swap_chars(decrypted_text, 'Ф', 'Щ')
        decrypted_text = swap_chars(decrypted_text, 'Ъ', 'Ш')


        write_results(decrypted_text, found_key)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()