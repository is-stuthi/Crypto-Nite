# Crypto Nite - Day 4

## Topics Covered

- Polyalphabetic Ciphers
- Vigenère Cipher
- Repeating Keys
- Modular Arithmetic in Vigenère Cipher
- Vigenère Cipher Implementation in Python

---

## Why Move Beyond Monoalphabetic Ciphers?

In monoalphabetic substitution ciphers, each plaintext letter always maps to the same ciphertext letter. Although this is more secure than the Caesar cipher, it still preserves the frequency distribution of letters, making it vulnerable to frequency analysis.

The Vigenère cipher overcomes this limitation by using multiple Caesar shifts determined by a secret key, allowing the same plaintext letter to encrypt to different ciphertext letters.

---

## What is a Polyalphabetic Cipher?

A polyalphabetic cipher uses multiple substitution alphabets instead of a single fixed substitution.

Unlike monoalphabetic ciphers, the encryption changes throughout the message based on a repeating key, making frequency analysis much more difficult.

---

## How Does the Vigenère Cipher Work?

The Vigenère cipher encrypts each character using a shift determined by the corresponding character of a repeating keyword.

For example:

**Plaintext**

```
HELLOWORLD
```

**Key**

```
KEYKEYKEYK
```

Each key character acts as the shift value for encrypting the corresponding plaintext character.

---

## Role of Modular Arithmetic

Each alphabet letter is converted into a number from 0–25.

Encryption:

```
Ci = (Pi + Ki) mod 26
```

Decryption:

```
Pi = (Ci - Ki) mod 26
```

Modular arithmetic ensures that the alphabet wraps around correctly whenever the shift exceeds 'Z'.

---

## Why is the Vigenère Cipher Stronger?

Compared to the Caesar and monoalphabetic substitution ciphers, the Vigenère cipher:

- Uses multiple shift values instead of one.
- Encrypts identical plaintext letters differently depending on their position.
- Makes simple frequency analysis much less effective.

---

## Limitations

The Vigenère cipher is still not unbreakable.

If the key is short and repeats frequently, attackers can exploit repeating patterns using techniques such as the **Kasiski Examination** and the **Friedman Test** to recover the key.

---

## What I Built Today

- Implemented repeating key generation.
- Implemented Vigenère Cipher encryption.
- Implemented Vigenère Cipher decryption.
- Preserved uppercase and lowercase letters.
- Preserved spaces, numbers and punctuation.
- Used modular arithmetic to perform encryption and decryption.

---

## Future Improvements

- Update the implementation so that spaces and punctuation do not consume key characters, matching the standard Vigenère cipher implementation.
- Add input validation to ensure the key contains only alphabetic characters.
- Add more test cases to verify edge cases and different input formats.