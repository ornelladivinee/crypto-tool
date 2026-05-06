from ciphers import caesar

# =========================
# BRUTE FORCE ATTACK (CAESAR)
# =========================

def brute_force_caesar(text):

    results = []

    # probamos todas las claves posibles
    for key in range(1, 26):

        # intentamos descifrar
        decrypted = caesar(text, key, "decrypt")

        # guardamos resultado
        results.append((key, decrypted))

    return results