from ciphers import caesar, vigenere
from logger import log_action
from analyzer import detect_cipher
from attack import brute_force_caesar

while True:
    print("\n=== CRYPTO TOOL v2 ===")
    print("1. Caesar Cipher")
    print("2. Vigenere Cipher")
    print("3. Detect Cipher")
    print("4. Brute Force Caesar")
    print("5. Exit")

    option = input("Choose: ")

    if option == "1":
        text = input("Text: ")
        key = int(input("Key: "))
        mode = input("encrypt/decrypt: ")

        result = caesar(text, key, mode)
        print(result)
        log_action("caesar", text, result)

    elif option == "2":
        text = input("Text: ")
        key = input("Key: ")
        mode = input("encrypt/decrypt: ")

        result = vigenere(text, key, mode)
        print(result)
        log_action("vigenere", text, result)

    elif option == "3":
        text = input("Text: ")
        print("Detected:", detect_cipher(text))

    elif option == "4":
        text = input("Text to crack: ")

        results = brute_force_caesar(text)

        print("\n--- Brute Force Results ---")
        for key, result in results:
            print(f"Key {key}: {result}")

    elif option == "5":
        break