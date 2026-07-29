# Crypto Nite - Day 6

## Topics Covered

* Hill Cipher
* Polygraphic Substitution Cipher
* Matrix Representation of Plaintext
* Matrix Multiplication
* Modular Arithmetic
* Matrix Inverse
* Encryption and Decryption
* Conditions for a Valid Key Matrix
* Python Implementation of Hill Cipher

---

## What is the Hill Cipher?

The Hill Cipher is a **classical polygraphic substitution cipher** invented by Lester S. Hill in 1929.

Unlike the Caesar, Monoalphabetic, Vigenère and Playfair ciphers, which rely on substitution rules, the Hill Cipher encrypts **blocks of letters** using **matrix multiplication** and **modular arithmetic**.

It is one of the first classical ciphers to introduce concepts from **linear algebra** into cryptography.

---

## Why was the Hill Cipher introduced?

Earlier substitution ciphers operate on one or two letters at a time, making them vulnerable to frequency analysis.

The Hill Cipher improves security by encrypting an entire block of letters simultaneously using a mathematical transformation.

This diffuses the relationship between plaintext and ciphertext, making statistical attacks more difficult than on earlier classical ciphers.

---

## Letter to Number Mapping

Before encryption, every letter is converted into its numerical equivalent.

```
A = 0
B = 1
C = 2
...
Z = 25
```

Example:

```
HI

↓

H = 7
I = 8

↓

[7]
[8]
```

---

## The Key Matrix

The Hill Cipher uses a square matrix as the encryption key.

For a 2 × 2 Hill Cipher, a key matrix looks like:

```
|3 3|
|2 5|
```

The size of the matrix determines the number of letters encrypted together.

* 2 × 2 matrix → 2-letter blocks
* 3 × 3 matrix → 3-letter blocks
* n × n matrix → n-letter blocks

---

## Preparing the Plaintext

Before encryption, the plaintext must be processed.

Rules:

* Convert all letters to uppercase.
* Remove spaces and other non-alphabetic characters.
* Split the plaintext into blocks based on the matrix size.
* If the final block is incomplete, append **X** as padding.

Example:

```
HELLO

↓

HELLOX

↓

HE
LL
OX
```

---

## Encryption

Encryption is performed using the formula

```
C = K × P (mod 26)
```

where

* **K** = Key Matrix
* **P** = Plaintext Vector
* **C** = Ciphertext Vector

Example:

```
Plaintext : HI

↓

[7]
[8]
```

Using the key matrix

```
|3 3|
|2 5|
```

Matrix multiplication:

```
|3 3|   |7|   |45|
|2 5| × |8| = |54|
```

Taking modulo 26:

```
45 mod 26 = 19
54 mod 26 = 2
```

Ciphertext:

```
19 → T
2  → C

↓

TC
```

---

## Why Modulo 26?

Matrix multiplication often produces values larger than 25.

Since the English alphabet contains only 26 letters, every value is reduced using modulo 26.

Example:

```
45 mod 26 = 19

54 mod 26 = 2
```

This keeps every encrypted value between **0** and **25**.

---

## Decryption

Decryption uses the inverse of the key matrix.

```
P = K⁻¹ × C (mod 26)
```

Unlike ordinary numbers, matrices cannot be divided.

Instead, the ciphertext is multiplied by the **inverse key matrix** to recover the original plaintext.

---

## Inverse Key Matrix

For a matrix

```
|a b|
|c d|
```

its inverse is

```
        1
---------------- × | d  -b |
(ad − bc)         | -c  a  |
```

Since the Hill Cipher works modulo 26, ordinary division is replaced by the **modular multiplicative inverse** of the determinant.

---

## Conditions for a Valid Key Matrix

Not every matrix can be used as a Hill Cipher key.

A valid key matrix must satisfy the following conditions:

* The determinant must not be zero.
* The determinant must have a modular inverse modulo 26.
* Equivalently,

```
gcd(det(K), 26) = 1
```

If these conditions are not satisfied, the plaintext cannot be recovered during decryption.

---

## Advantages

* Encrypts multiple letters simultaneously.
* Stronger than simple substitution ciphers against frequency analysis.
* Introduces linear algebra into cryptography.
* Supports different block sizes.

---

## Limitations

* Requires an invertible key matrix.
* Matrix calculations become more complex as the block size increases.
* Vulnerable to known-plaintext attacks.
* Not considered secure by modern cryptographic standards.

---

## What I built today

* Implemented the Hill Cipher using a 2 × 2 key matrix.
* Converted plaintext into numerical vectors.
* Performed matrix multiplication for encryption.
* Implemented decryption using the inverse key matrix.
* Added plaintext padding for incomplete blocks.
* Validated key matrices before encryption and decryption.

---

## Key Takeaways

* Hill Cipher encrypts blocks of letters rather than individual characters.
* Plaintext is represented as numerical vectors.
* Matrix multiplication is used to generate the ciphertext.
* Modulo 26 keeps all values within the alphabet.
* Decryption requires the inverse of the key matrix.
* Only matrices with an invertible determinant modulo 26 are valid encryption keys.
