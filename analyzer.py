def detect_cipher(text):
    letters = [c for c in text.lower() if c.isalpha()]

    if len(letters) == 0:
        return "unknown"

    # heurística simple:
    if " " in text and len(set(text)) < 15:
        return "caesar_likely"

    return "vigenere_or_unknown"