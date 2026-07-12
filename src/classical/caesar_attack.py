def brute_force(ciphertext):
    #Trying all 26 possible Caesar shifts to recover plaintext
    print("The possible plaintexts are:\n")
    for i in range(0,26):
        plaintext=""
        for char in ciphertext:
            if char.isupper():
                plaintext+=chr((ord(char)-65-i)%26 + 65)
            elif char.islower():
                 plaintext+=chr((ord(char)-97-i)%26 + 97)
            else:
                plaintext+=char
        print(f"Shift {i:2}:{plaintext}")

def main():
    print("Cryptanalysis of Caesar Cipher")
    print("===============================")
    print("Enter the cipher text:")
    ciphertext=input()
    brute_force(ciphertext)
    
if __name__ == "__main__":
    main()