import random

plain="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_key():
    alphabet=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabet)
    return "".join(alphabet)

def encrypt(key,message):
    encrypted=""  
    for char in message:
        if char.isupper():
            index=plain.find(char)
            encrypted+=key[index]
        elif char.islower():
            index=plain.find(char.upper())
            encrypted+=key[index].lower()
        else:
            encrypted+=char
    return encrypted

def decrypt(key,message):
    decrypted=""
    for char in message:
        if char.isupper():
            index=key.find(char)
            decrypted+=plain[index]
        elif char.islower():
            index=key.find(char.upper())
            decrypted+=plain[index].lower()
        else:
            decrypted+=char
    return decrypted

def main():
    print("Monoalphabetic Cipher")
    print("=====================")
    print("Enter message to be encrypted:")
    message=input()
    key=generate_key()
    print(f"Key generated:{key}")
    ciphertext=encrypt(key,message)
    print(f"Encrypted text:{ciphertext}")
    print("Enter message to be decrypted:")
    message=input()
    print(f"Using key:{key}")
    plaintext=decrypt(key,message)
    print(f"Decrypted text:{plaintext}")

if __name__ == "__main__":
    main()