# Crypto Nite - Day 3

## Topics Covered

* Monoalphabetic Substitution Cipher
* Advantages over Caesar Cipher
* Weaknesses of Monoalphabetic Cipher
* Frequency Analysis
* Python Implementation of Monoalphabetic Cipher
* Frequency Analysis Implementation in Python

---

## What is a Monoalphabetic Substitution Cipher?

A Monoalphabetic Substitution Cipher is a classical encryption technique that relies on a fixed, **one-to-one mapping** across the entire alphabet. Unlike the Caesar Cipher, which shifts the entire alphabet uniformly by a static numeric offset, a monoalphabetic cipher maps each plaintext character to a completely distinct ciphertext character.

* **Secret Key:** A specific permutation of the characters A–Z (all 26 letters arranged in a random order with no duplicates).
* **Core Rule:** Once a mapping is established, every occurrence of a particular plaintext letter is replaced by the exact same ciphertext letter throughout the entire message.

---

## Why is it stronger than the Caesar Cipher?

The strength of a Monoalphabetic Substitution Cipher comes from its significantly larger **key space** compared to the Caesar Cipher.

* The **Caesar Cipher** has only **25 non-trivial keys** (ignoring a shift of 0), making it vulnerable to a simple **brute-force attack**, where every possible key is tried until the correct plaintext is recovered.
* A **Monoalphabetic Substitution Cipher** allows every letter of the alphabet to be rearranged independently. The total number of possible keys is equal to the number of permutations of the 26-letter alphabet:

```text
Key Space = 26!
          = 26 × 25 × 24 × ... × 1
          ≈ 4.03 × 10²⁶ possible keys
```

This enormous key space makes an exhaustive brute-force search computationally impractical. However, a large key space alone does **not** guarantee security. Since the substitution remains fixed throughout the message, the cipher preserves the statistical characteristics of the plaintext, allowing it to be broken using frequency analysis instead of brute force.

---

## The Fatal Flaw: Why it is still insecure

Despite its resistance to brute-force attacks, the cipher remains fundamentally insecure because **it preserves the statistical properties of the plaintext language**.

Since the substitution is fixed and one-to-one, every occurrence of the same plaintext letter is always replaced by the same ciphertext letter. As a result, linguistic patterns remain visible in the encrypted text.

### 1. Single-Letter Frequency Analysis

Letters in English do not occur with equal probability.

Some letters naturally appear much more frequently than others.

* **High-frequency letters:** `E` (~12.7%), followed by `T`, `A`, `O`, `I`, `N`, `S`, `H`, `R`.
* **Low-frequency letters:** `Q`, `J`, `X`, `Z`.

An attacker can count the occurrence of each ciphertext letter and compare it with known English letter frequencies.

For example, if the ciphertext letter `Q` appears approximately 13% of the time, it is likely representing the plaintext letter `E`.

---

### 2. Digraphs and Trigraphs (N-grams)

Natural languages contain recurring groups of letters.

Some common **digraphs** are:

* `TH`
* `HE`
* `IN`
* `ER`
* `AN`
* `RE`

Some common **trigraphs** are:

* `THE`
* `AND`
* `ING`
* `ENT`
* `ION`

Even though the letters are substituted, these repeated patterns remain. Identifying frequently occurring pairs and triplets helps narrow down the substitution mapping.

---

### 3. Pattern Matching (Word Structure)

Repeated letter patterns reveal information about possible words.

Examples include:

* **Double letters:** Words such as `HELLO`, `BOOK`, and `SHEEP` contain repeated letters (`LL`, `OO`, `EE`). These repetitions remain visible after substitution.
* **Short words:** Common two-letter and three-letter words like `OF`, `TO`, `IN`, `THE`, and `AND` occur frequently and provide valuable clues.
* **Repeated letter structures:** Words with identical structural patterns can often be identified even when every letter has been substituted.

Pattern matching, combined with frequency analysis, allows an attacker to gradually reconstruct the entire substitution alphabet.

---

## What I Built Today

* Implemented a random key generator for a Monoalphabetic Substitution Cipher.
* Implemented encryption using a substitution alphabet.
* Implemented decryption by reversing the substitution mapping.
* Preserved uppercase and lowercase letters.
* Preserved spaces, numbers and punctuation.
* Generated a random valid substitution key for each execution instead of accepting a user-defined key.
* Built a frequency analysis tool using Python's `Counter` class.
* Learned why increasing the key space alone does not guarantee security.
