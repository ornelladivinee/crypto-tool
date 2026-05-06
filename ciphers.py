alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar(text, key, mode):
    result = ""
    key = key % 26

    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())

            if mode == "encrypt":
                new_index = (index + key) % 26
            else:
                new_index = (index - key) % 26

            new_char = alphabet[new_index]
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char

    return result


def vigenere(text, key, mode):
    result = ""
    key = key.lower()
    key_index = 0

    for char in text:
        if char.lower() in alphabet:

            text_index = alphabet.index(char.lower())
            key_char = key[key_index % len(key)]
            key_shift = alphabet.index(key_char)

            if mode == "encrypt":
                new_index = (text_index + key_shift) % 26
            else:
                new_index = (text_index - key_shift) % 26

            new_char = alphabet[new_index]
            result += new_char.upper() if char.isupper() else new_char

            key_index += 1
        else:
            result += char

    return result