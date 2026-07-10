def encrypt():
    print("Enter the message to encrypt:")
    message = input()
    print("Enter the shift value:")
    shift = int(input())
    encrypted=""
    for char in message:
        #If character is an uppercase letter
        #65 because ASCII value of 'A' is 65
        if char.isupper():
            encrypted+=chr((ord(char) + shift - 65) % 26 + 65)
        #If character is a lowercase letter
        #97 because ASCII value of 'a' is 97
        elif char.islower():
            encrypted+=chr((ord(char) + shift - 97) % 26 + 97)
        #Don't change any other character
        else:
            encrypted+=char
    return encrypted
    
def decrypt():
    print("\nEnter the message to decrypt:")
    message = input()
    print("Enter the shift value:")
    shift = int(input())
    decrypted=""
    for char in message:
        #If character is an uppercase letter
        if char.isupper():
            decrypted+=chr((ord(char)-shift-65)%26+65)  
        #If charcter is a lowercase letter
        elif char.islower():
            decrypted+=chr((ord(char)-shift-97)%26+97)
        #No change for any other character
        else:
            decrypted+=char
    return decrypted

def main():
    print("CAESAR CIPHER")
    print("==============")
    print("Choices:\n1 to encrypt\n2 to decrypt\n3 to Exit")
    while True:
        print("Enter your choice:")
        choice = int(input()) 
        if choice == 1:
            ciphertext=encrypt()
            print("Encrypted message:", ciphertext, "\n")
        elif choice == 2:
            plaintext=decrypt()
            print("Decrypted message:", plaintext, "\n")
        elif choice == 3:
            print("\nThank you!")
            break # Breaks out of the loop to exit the program
        else:
            print("Please enter valid choice.\n")
    
if __name__ == "__main__":
    main()
          