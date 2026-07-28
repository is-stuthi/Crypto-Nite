def generate_matrix(key):
    key = key.upper().replace("J", "I")

    sequence = []

    for char in key:
        if char.isalpha() and char not in sequence:
            sequence.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in sequence:
            sequence.append(char)

    matrix = []
    for i in range(0, 25, 5):
        matrix.append(sequence[i:i + 5])

    return matrix


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(char for char in text if char.isalpha())

    prepared = ""
    i = 0

    while i < len(text):
        first = text[i]

        if i + 1 == len(text):
            second = "X"
            i += 1

        else:
            second = text[i + 1]

            if first == second:
                second = "X"
                i += 1
            else:
                i += 2

        prepared += first + second

    return prepared


def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col


def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return (
            matrix[row1][(col1 + 1) % 5],
            matrix[row2][(col2 + 1) % 5]
        )

    elif col1 == col2:
        return (
            matrix[(row1 + 1) % 5][col1],
            matrix[(row2 + 1) % 5][col2]
        )

    else:
        return (
            matrix[row1][col2],
            matrix[row2][col1]
        )


def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return (
            matrix[row1][(col1 - 1) % 5],
            matrix[row2][(col2 - 1) % 5]
        )

    elif col1 == col2:
        return (
            matrix[(row1 - 1) % 5][col1],
            matrix[(row2 - 1) % 5][col2]
        )

    else:
        return (
            matrix[row1][col2],
            matrix[row2][col1]
        )


def encrypt(key, message):
    matrix = generate_matrix(key)
    message = prepare_text(message)

    ciphertext = ""

    for i in range(0, len(message), 2):
        a, b = encrypt_pair(matrix, message[i], message[i + 1])
        ciphertext += a + b

    return ciphertext


def decrypt(key, message):
    matrix = generate_matrix(key)

    plaintext = ""

    for i in range(0, len(message), 2):
        a, b = decrypt_pair(matrix, message[i], message[i + 1])
        plaintext += a + b

    return plaintext


def print_matrix(matrix):
    print("\nKey Matrix:")
    for row in matrix:
        print(" ".join(row))


def main():
    print("Playfair Cipher")
    print("================")

    key = input("Enter key: ")
    plaintext = input("Enter message to be encrypted: ")

    matrix = generate_matrix(key)
    print_matrix(matrix)

    ciphertext = encrypt(key, plaintext)

    print(f"\nPrepared Text : {prepare_text(plaintext)}")
    print(f"Encrypted Text: {ciphertext}")

    print("\nEnter message to be decrypted:")
    message = input()

    plaintext = decrypt(key, message)

    print(f"Decrypted Text: {plaintext}")


if __name__ == "__main__":
    main()

"""
Sample Run

Enter key: MONARCHY
Enter message to be encrypted: HELLO WORLD

Key Matrix:
M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z

Prepared Text : HELXLOWORLDX
Encrypted Text: CFSUPMVNMTBZ

Enter message to be decrypted:
CFSUPMVNMTBZ

Decrypted Text: HELXLOWORLDX
"""