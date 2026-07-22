# Crypto Nite - Day 4

## Topics Covered

- Introduction to Polyalphabetic Ciphers
- Vigenère Cipher
- Repeating Key Generation
- Mathematical Formulation
- Advantages and Limitations

---

## Why Move Beyond Monoalphabetic Ciphers?

In monoalphabetic substitution ciphers, every occurrence of a plaintext letter is always replaced by the same ciphertext letter. Although this is much stronger than the Caesar cipher, it is still vulnerable to frequency analysis because letter frequencies remain unchanged.

The Vigenère cipher addresses this weakness by using multiple substitution alphabets, causing the same plaintext letter to encrypt to different ciphertext letters depending on its position.

---

## What is a Polyalphabetic Cipher?

A polyalphabetic cipher uses multiple substitution alphabets during encryption instead of relying on a single fixed substitution.

Unlike monoalphabetic ciphers, the mapping between plaintext and ciphertext changes throughout the message based on a secret key.

---

## Vigenère Cipher

The Vigenère cipher is one of the most well-known polyalphabetic substitution ciphers.

Instead of applying one constant shift, it applies different Caesar shifts determined by a repeating keyword.

### Example

**Plaintext**

```
HELLOWORLD
```

**Key**

```
KEYKEYKEYK
```

Each key letter determines the shift used for encrypting the corresponding plaintext character.

---

## Mathematical Representation

Encryption:

```
Ci = (Pi + Ki) mod 26
```

Decryption:

```
Pi = (Ci - Ki) mod 26
```

where:

- Pi = Plaintext letter
- Ki = Key letter
- Ci = Ciphertext letter

---

## Advantages

- Stronger than Caesar cipher
- Stronger than monoalphabetic substitution
- Makes frequency analysis significantly more difficult
- Same plaintext letter can encrypt to different ciphertext letters

---

## Limitations

- Security depends on the secrecy and length of the key.
- Repeated keys introduce patterns that can be exploited.
- Vulnerable to cryptanalysis techniques such as the Kasiski Examination and Friedman Test.

---

## Python Implementation

Current progress:

- Implemented repeating key generation.
- Encryption and decryption functions will be completed next.

---

## Key Takeaways

- The Vigenère cipher introduced the concept of polyalphabetic substitution.
- Using multiple shifting alphabets greatly improves security compared to earlier classical ciphers.
- Although historically significant, it can still be broken using modern cryptanalysis techniques.