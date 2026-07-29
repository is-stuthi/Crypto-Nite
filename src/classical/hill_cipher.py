def text_to_numbers(text):
    return [ord(char) - ord("A") for char in text]


def numbers_to_text(numbers):
    return "".join(chr(num + ord("A")) for num in numbers)


def prepare_text(text):
    text = text.upper()
    text = "".join(char for char in text if char.isalpha())

    while len(text) % 2 != 0:
        text += "X"

    return text


def multiply_matrix_vector(matrix, vector):
    result = []

    for row in matrix:
        value = 0

        for i in range(2):
            value += row[i] * vector[i]

        result.append(value % 26)

    return result


def inverse_key_matrix(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    determinant = (a * d - b * c) % 26

    if determinant == 0:
        raise ValueError("Invalid key matrix! Determinant is 0.")

    try:
        determinant_inverse = pow(determinant, -1, 26)
    except ValueError:
        raise ValueError("Invalid key matrix! Determinant has no modular inverse modulo 26.")

    inverse = [
        [d, -b],
        [-c, a]
    ]

    for i in range(2):
        for j in range(2):
            inverse[i][j] = (inverse[i][j] * determinant_inverse) % 26

    return inverse


def encrypt(key_matrix, plaintext):
    plaintext = prepare_text(plaintext)

    numbers = text_to_numbers(plaintext)

    ciphertext = []

    for i in range(0, len(numbers), 2):
        block = numbers[i:i + 2]
        encrypted = multiply_matrix_vector(key_matrix, block)
        ciphertext.extend(encrypted)

    return numbers_to_text(ciphertext)


def decrypt(key_matrix, ciphertext):
    ciphertext = prepare_text(ciphertext)

    inverse_matrix = inverse_key_matrix(key_matrix)

    numbers = text_to_numbers(ciphertext)

    plaintext = []

    for i in range(0, len(numbers), 2):
        block = numbers[i:i + 2]
        decrypted = multiply_matrix_vector(inverse_matrix, block)
        plaintext.extend(decrypted)

    return numbers_to_text(plaintext)


def print_matrix(matrix):
    print("\nKey Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    print("Hill Cipher")
    print("===========")

    print("\nEnter the 2×2 key matrix:")

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))

    key_matrix = [
        [a, b],
        [c, d]
    ]

    try:
        inverse_key_matrix(key_matrix)
    except ValueError as e:
        print(f"\nError: {e}")
        return

    print_matrix(key_matrix)

    plaintext = input("\nEnter message to be encrypted: ")

    ciphertext = encrypt(key_matrix, plaintext)

    print(f"\nPrepared Text : {prepare_text(plaintext)}")
    print(f"Encrypted Text: {ciphertext}")

    ciphertext = input("\nEnter message to be decrypted: ")

    decrypted = decrypt(key_matrix, ciphertext)

    print(f"Decrypted Text: {decrypted}")


if __name__ == "__main__":
    main()


"""
Sample Run

Hill Cipher
===========

Enter the 2×2 key matrix:
a: 3
b: 3
c: 2
d: 5

Key Matrix:
3 3
2 5

Enter message to be encrypted: HELLO

Prepared Text : HELLOX
Encrypted Text: HIOZHN

Enter message to be decrypted:
HIOZHN

Decrypted Text: HELLOX
"""