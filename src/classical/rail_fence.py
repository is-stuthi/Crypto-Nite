def encrypt(plaintext, rails):
    if rails <= 1 or rails >= len(plaintext):
        return plaintext

    rail_list = [""] * rails

    current_rail = 0
    direction = 1  # 1 = down, -1 = up

    for char in plaintext:
        rail_list[current_rail] += char

        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1

        current_rail += direction

    ciphertext = "".join(rail_list)
    return ciphertext


def decrypt(ciphertext, rails):
    if rails <= 1 or rails >= len(ciphertext):
        return ciphertext

    # Create an empty matrix
    matrix = [["" for _ in range(len(ciphertext))] for _ in range(rails)]

    # Mark the zig-zag path
    current_rail = 0
    direction = 1

    for col in range(len(ciphertext)):
        matrix[current_rail][col] = "*"

        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1

        current_rail += direction

    # Fill the marked positions with ciphertext
    index = 0
    for row in range(rails):
        for col in range(len(ciphertext)):
            if matrix[row][col] == "*":
                matrix[row][col] = ciphertext[index]
                index += 1

    # Read the zig-zag to recover plaintext
    plaintext = ""

    current_rail = 0
    direction = 1

    for col in range(len(ciphertext)):
        plaintext += matrix[current_rail][col]

        if current_rail == 0:
            direction = 1
        elif current_rail == rails - 1:
            direction = -1

        current_rail += direction

    return plaintext


def main():
    print("Rail Fence Cipher")
    print("=================")

    print("1. Encrypt")
    print("2. Decrypt")

    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        plaintext = input("Enter the plaintext: ")
        rails = int(input("Enter the number of rails: "))

        ciphertext = encrypt(plaintext, rails)

        print("\nCiphertext:", ciphertext)

    elif choice == "2":
        ciphertext = input("Enter the ciphertext: ")
        rails = int(input("Enter the number of rails: "))

        plaintext = decrypt(ciphertext, rails)

        print("\nPlaintext:", plaintext)

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()