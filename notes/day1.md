# Crypto Nite - Day 1

## Topics Covered
- Introduction to Cryptography
- Plaintext, Ciphertext and Keys
- Modular Arithmetic
- Caesar Cipher
- Caesar Cipher Implementation in Python

---

## Why Cryptography?

Cryptography protects information during communication by ensuring:

- **Confidentiality:** Only the intended recipient can read the message.
- **Integrity:** The message is not modified while being transmitted.
- **Authentication:** The communicating entities can verify each other's identity.
- **Non-repudiation:** A sender cannot later deny sending a message.

---

## Main Components of Cryptography

### Plaintext
The original readable message.

### Ciphertext
The encrypted (scrambled) version of the plaintext.

### Key
A secret value used by the encryption algorithm to convert plaintext into ciphertext (and vice versa).

---

## Why is the Caesar Cipher weak?

The Caesar Cipher has only **25 possible keys** (ignoring a shift of 0). An attacker could simply try every possible shift until the message becomes readable (brute-force attack).

Once the shift value is known, anyone can decrypt messages or even encrypt fake messages pretending to be the original sender.

---

## Role of Modular Arithmetic

The alphabet contains only 26 letters.

Modular arithmetic allows the encryption process to "wrap around" when shifting beyond 'Z' or 'z'.

For example:

25 + 3 = 28

28 mod 26 = 2

which means 'Z' shifted by 3 becomes 'C'.

It also means shift values larger than 26 are handled naturally. For example, a shift of 29 is equivalent to a shift of 3.

---

## How would I break the Caesar Cipher if I didn't know the key?

Since there are only 25 possible shifts, I would try every possible key and read each resulting message until one produces meaningful English text.

This is called a **brute-force attack**.

---

## What I built today

- Implemented Caesar Cipher encryption.
- Implemented Caesar Cipher decryption.
- Supported uppercase and lowercase letters.
- Preserved spaces, numbers and punctuation.
- Built a menu-driven Python application.
- Learned how `ord()`, `chr()` and modulo arithmetic work together to perform encryption.