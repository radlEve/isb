def decrypt(encoded_text:str, key: dict) -> str:
    decrypted = []
    for char in encoded_text:
        decrypted.append(key.get(char, char))
    return ''.join(decrypted)