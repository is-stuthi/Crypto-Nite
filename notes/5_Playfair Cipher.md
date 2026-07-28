# Crypto Nite - Day 5

## Topics Covered
- Playfair Cipher
- Digraph (Pair-wise) Encryption
- 5 × 5 Key Matrix
- Preparing Plaintext
- Encryption Rules
- Decryption Rules
- Python Implementation of Playfair Cipher

---

## What is the Playfair Cipher?

The Playfair Cipher is a **classical substitution cipher** that encrypts **pairs of letters (digraphs)** instead of individual letters.

Unlike the Caesar, Monoalphabetic and Vigenère ciphers, which substitute one character at a time, Playfair encrypts two characters together using their positions inside a **5 × 5 key matrix**.

This makes frequency analysis more difficult because attackers must analyze letter pairs instead of individual letters.

---

## Why was the Playfair Cipher introduced?

Although the Vigenère Cipher is much stronger than the Caesar Cipher, repeated patterns can still leak information.

The Playfair Cipher improves security by encrypting **two letters at a time**, reducing the effectiveness of simple frequency analysis.

---

## Constructing the Key Matrix

The Playfair Cipher uses a **5 × 5 matrix** generated from a keyword.

Steps:

1. Convert the keyword to uppercase.
2. Replace every **J** with **I**.
3. Remove duplicate letters from the keyword.
4. Fill the remaining cells using the unused letters of the alphabet.
5. Since there are 26 English letters but only 25 cells, **I** and **J** share the same position.

Example:

```
Keyword: MONARCHY

M O N A R
C H Y B D
E F G I K
L P Q S T
U V W X Z
```

---

## Preparing the Plaintext

Before encryption, the plaintext must be processed.

Rules:

- Convert all letters to uppercase.
- Replace every **J** with **I**.
- Remove spaces and other non-alphabetic characters.
- Split the message into pairs (digraphs).
- If both letters in a pair are identical, insert **X** between them.
- If one letter remains at the end, append **X**.

Example:

```
HELLO

↓

HE LX LO
```

Example:

```
DOG

↓

DO GX
```

---

## Encryption Rules

Each pair of letters follows exactly one of three rules.

### 1. Same Row

If both letters are in the same row, replace each letter with the letter immediately to its right.

Wrap around to the beginning of the row if necessary.

Example:

```
M O N A R

MR

↓

OM
```

---

### 2. Same Column

If both letters are in the same column, replace each letter with the letter immediately below it.

Wrap around to the top if necessary.

Example:

```
C
E

↓

EL
```

---

### 3. Rectangle Rule

If the letters are in different rows and different columns, they form the opposite corners of a rectangle.

Replace each letter with the letter in the **same row** but in the **other letter's column**.

Example:

```
M O
C H

MH

↓

OC
```

---

## Decryption Rules

Decryption follows the reverse process.

- Same Row → Shift Left
- Same Column → Shift Up
- Rectangle Rule → Remains the same

---

## Advantages

- Encrypts pairs of letters instead of individual characters.
- Makes single-letter frequency analysis less effective.
- More secure than the Caesar and Monoalphabetic substitution ciphers.

---

## Limitations

- **I** and **J** cannot be distinguished.
- Padding characters (usually **X**) may appear after decryption.
- Still vulnerable to digraph frequency analysis.
- Not considered secure by modern cryptographic standards.

---

## What I built today

- Generated a 5 × 5 Playfair key matrix from a keyword.
- Implemented plaintext preprocessing.
- Implemented Playfair encryption.
- Implemented Playfair decryption.
- Supported user-defined keys and plaintext.
- Learned how coordinate-based substitution differs from character-by-character substitution.

## Key Takeaways

- Playfair encrypts pairs of letters instead of single letters.
- Every pair always falls into exactly one of three cases: same row, same column or rectangle.
- The cipher relies on the positions of letters in a key matrix rather than alphabetical shifts.