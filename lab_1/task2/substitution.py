from constants import LETTER_FREQUENCIES, ENCRYPTED_ALPHABET


def frequency_analysis(encoded_text: str) -> dict[str, float]:
    """
    Анализировать частоту появления букв из алфавита зашифрованного текста
    :param encoded_text: зашифрованный текст
    :return: словарь, содержащий частоту появления
        для каждого символа зашифрованного текста
    """
    freq = {}
    for char in encoded_text:
        if char in ENCRYPTED_ALPHABET:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

    total = sum(freq.values())
    return {char: count / total for char, count in freq.items()}


def get_frequency_key(encoded_text: str) -> dict:
    """
    Расшифровать текст согласно частотам появления в нем определенных символов,
        сопоставляя с частотами появления букв русского алфавита
    :param encoded_text: зашифрованный текст
    :return: ключ, сопоставляющий буквы шифротекста и исходного текста
    """
    encoded_freq = frequency_analysis(encoded_text)

    sorted_encoded = sorted(encoded_freq, key=encoded_freq.get, reverse=True)
    sorted_standard = sorted(LETTER_FREQUENCIES, key=LETTER_FREQUENCIES.get, reverse=True)

    key = {enc_char: std_char for enc_char, std_char in zip(sorted_encoded, sorted_standard)}

    return key


def decrypt(encoded_text:str, key: dict) -> str:
    decrypted = []
    for char in encoded_text:
        decrypted.append(key.get(char, char))
    return ''.join(decrypted)