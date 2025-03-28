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


def decrypt(encoded_text: str) -> tuple[str, dict]:
    """
    Расшифровать текст согласно частотам появления в нем определенных символов,
        сопоставляя с частотами появления букв русского алфавита
    :param encoded_text: зашифрованный текст
    :return: кортеж, состоящий из расшифрованного текста и ключа для расшифровки
    """
    encoded_freq = frequency_analysis(encoded_text)

    sorted_encoded = sorted(encoded_freq, key=encoded_freq.get, reverse=True)
    sorted_standard = sorted(LETTER_FREQUENCIES, key=LETTER_FREQUENCIES.get, reverse=True)

    key = {enc_char: std_char for enc_char, std_char in zip(sorted_encoded, sorted_standard)}

    decrypted = []
    for char in encoded_text:
        decrypted.append(key.get(char, char))
    return ''.join(decrypted), key