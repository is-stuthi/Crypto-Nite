# Crypto Nite - Day 7

## Topics Covered

* Introduction to Transposition Ciphers
* Rail Fence Cipher
* Zig-Zag Pattern
* Encryption Process
* Decryption Process
* Time Complexity
* Advantages
* Limitations
* Python Implementation of Rail Fence Cipher

---

## What is a Transposition Cipher?

Until now, every cipher we have studied—Caesar, Monoalphabetic Substitution, Vigenère, Playfair and Hill Cipher—encrypted messages by **replacing** characters with different characters.

A **Transposition Cipher** follows a completely different approach.

Instead of changing the characters themselves, it **rearranges their positions** according to a specific rule. Every character from the plaintext appears exactly once in the ciphertext; only their order changes.

The Rail Fence Cipher is one of the simplest and earliest examples of a transposition cipher.

---

## What is the Rail Fence Cipher?

The Rail Fence Cipher is a **classical transposition cipher** that writes the plaintext diagonally across multiple rows, called **rails**, in a zig-zag pattern.

After all the characters have been placed, the rows are read one by one to produce the ciphertext.

Unlike substitution ciphers, **the letters themselves are never changed**. Only their positions are rearranged.

The **number of rails** acts as the secret key.

---

## Zig-Zag Pattern

Suppose the plaintext is

```
HELLOWORLD
```

using **3 rails**.

The message is written diagonally as

```
H . . . O . . . L
. E . L . W . R .
. . L . . . O . . D
```

Reading each row from left to right gives

```
HOL
ELWR
LOD
```

Ciphertext:

```
HOLELWRLOD
```

---

## Encryption Process

Encryption consists of four simple steps.

### Step 1

Choose the number of rails.

Example:

```
Rails = 3
```

---

### Step 2

Write the plaintext diagonally across the rails in a zig-zag pattern.

The writing direction changes whenever the **top** or **bottom** rail is reached.

---

### Step 3

Continue until every character has been placed.

---

### Step 4

Read each rail from top to bottom and concatenate the rows.

The resulting string is the ciphertext.

---

## Decryption Process

Decryption is slightly more challenging because the zig-zag pattern is not directly available in the ciphertext.

The process consists of four steps.

### Step 1

Create an empty rail matrix with the required number of rows and columns.

---

### Step 2

Traverse the matrix in the same zig-zag pattern used during encryption and mark every position that should contain a character.

---

### Step 3

Fill the marked positions **row by row** using the ciphertext.

---

### Step 4

Traverse the zig-zag pattern once again and read the characters in the original writing order to recover the plaintext.

---

## Time Complexity

Both encryption and decryption process every character a constant number of times.

```
Encryption : O(n)
Decryption : O(n)
```

Space Complexity:

```
O(n)
```

---

## Advantages

* Very easy to understand and implement.
* Introduces the concept of transposition ciphers.
* Encrypts by rearranging character positions instead of replacing characters.
* Runs in linear time.
* Useful for learning classical cryptography.

---

## Limitations

* Very small key space (only the number of rails).
* Preserves the original letter frequencies.
* Easily broken using brute-force attacks.
* Not considered secure by modern cryptographic standards.

---

## What I built today

* Implemented Rail Fence Cipher encryption using a zig-zag traversal.
* Implemented Rail Fence Cipher decryption by reconstructing the zig-zag pattern.
* Used the number of rails as the encryption and decryption key.
* Preserved uppercase letters, lowercase letters, spaces, numbers and punctuation.
* Learned the difference between substitution and transposition ciphers.
* Learned how reconstructing the zig-zag pattern is the key idea behind decryption.

---

## Key Takeaways

* Rail Fence is a **transposition cipher**, not a substitution cipher.
* Characters are never modified; only their positions are rearranged.
* The number of rails acts as the secret key.
* Encryption writes the plaintext in a zig-zag pattern and reads it row by row.
* Decryption reconstructs the zig-zag pattern before reading the plaintext.
* Although historically important, the Rail Fence Cipher is not secure against modern cryptographic attacks.
