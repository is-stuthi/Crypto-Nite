def generate_repeating_key(message, key):
    repeats = (len(message) // len(key)) + 1
    return (key * repeats)[: len(message)]


def encrypt(message, r_key):
    cipher_text = []
    for i in range(len(message)):
        char = message[i]
        key_char = r_key[i]

        if char.isalpha():
            # Determine base ASCII value (65 for 'A', 97 for 'a')
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(key_char.upper()) - ord("A")

            # Apply shift with modular arithmetic
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            cipher_text.append(encrypted_char)
        else:
            # Leave non-alphabetical characters unchanged
            cipher_text.append(char)

    return "".join(cipher_text)


def decrypt(ciphertext, r_key):
    plain_text = []
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = r_key[i]

        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = ord(key_char.upper()) - ord("A")

            # Reverse the shift with modular arithmetic
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            plain_text.append(decrypted_char)
        else:
            plain_text.append(char)

    return "".join(plain_text)


if __name__ == "__main__":
    print("Vigenere Cipher")
    print("===============")
    print("Enter key:")
    key = input().strip()
    print("Enter message to encrypt:")
    message = input()

    r_key = generate_repeating_key(message, key)

    encrypted_msg = encrypt(message, r_key)
    print(f"\nEncrypted Message: {encrypted_msg}")

    decrypted_msg = decrypt(encrypted_msg, r_key)
    print(f"Decrypted Message: {decrypted_msg}")
    