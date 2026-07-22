"""
To be implemented:
- encrypt()
- decrypt()
"""


def generate_repeating_key(message, key):
    repeats = (len(message) // len(key)) + 1
    return (key * repeats)[: len(message)]

def encrypt(message, r_key):
    pass


def decrypt(ciphertext, r_key):
    pass


if __name__ == "__main__":
    print("Vigenere Cipher")
    print("===============")
    print("Enter key:")
    key=input()
    print("Enter message to encrypt:")
    message=input()
    r_key=generate_repeating_key(message, key)
    

    