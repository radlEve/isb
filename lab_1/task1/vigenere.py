from lab_1.task1.constants import ALPHABET, ALPHABET_LENGTH, REPLACEMENTS


def clean_text(text: str) -> str:
    text = text.upper()
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)
    return text


def encrypt(text: str, key: str) -> str:
    encrypted = []
    key = clean_text(key)
    text = clean_text(text)

    for i, char in enumerate(text.upper()):
        if char not in ALPHABET:
            raise ValueError(f"Символ '{char}' не входит в алфавит!")
        text_idx = ALPHABET.index(char)
        key_idx = ALPHABET.index(key[i % len(key)])
        encrypted.append(ALPHABET[(text_idx + key_idx) % ALPHABET_LENGTH])

    return ''.join(encrypted)