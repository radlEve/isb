from lab_1.task1.constants import ALPHABET, ALPHABET_LENGTH


def encrypt(text: str, key: str) -> str:
    encrypted = []
    key = key.upper().replace('Ё', 'Е')
    text = text.upper().replace('Ё', 'Е')
    text = text.upper().replace('!', '')
    text = text.upper().replace('?', '')
    text = text.upper().replace('.', '')
    text = text.upper().replace(',', '')

    for i, char in enumerate(text.upper()):
        if char not in ALPHABET:
            raise ValueError(f"Символ '{char}' не входит в алфавит!")
        text_idx = ALPHABET.index(char)
        key_idx = ALPHABET.index(key[i % len(key)])
        encrypted.append(ALPHABET[(text_idx + key_idx) % ALPHABET_LENGTH])

    return ''.join(encrypted)