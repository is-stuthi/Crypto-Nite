# Crypto Nite - Day 2

## Topics Covered

- Cryptanalysis
- Kerckhoffs's Principle
- Brute-Force Attack
- Frequency Analysis
- Brute-Force Attack Implementation in Python

---

## What is Cryptanalysis?

While **cryptography** focuses on securely encrypting and decrypting information, **cryptanalysis** is the process of analyzing cryptographic systems to find weaknesses.

The goal of cryptanalysis is to recover the original plaintext or determine the secret key without prior knowledge of the key.

---

## Kerckhoffs's Principle

A cryptographic system should remain secure even if everything about the system, except the key, is public knowledge.

In other words, the security of a cipher should depend only on keeping the **key** secret—not the encryption algorithm.

This principle forms the foundation of modern cryptography.

---

## What is a Brute-Force Attack?

A brute-force attack is a trial-and-error technique where every possible key is tested until the correct plaintext is obtained.

Unlike attacks that exploit mathematical weaknesses, brute force simply relies on trying every possible key.

---

## Why does Brute Force always work on the Caesar Cipher?

The Caesar Cipher has an extremely small key space.

Since the English alphabet contains only **26 letters**, there are only **26 possible shifts**.

Because the cipher uses **modulo 26 arithmetic**, any shift larger than 26 is simply a repetition of an earlier shift.

For example:

- Shift 1 is equivalent to Shift 27.
- Shift 5 is equivalent to Shift 31.

Therefore, an attacker only needs to test all 26 possible shifts to recover the plaintext.

---

## What is Frequency Analysis?

In English, certain letters appear much more frequently than others.

For example:

- E
- T
- A
- O
- I
- N

Since the Caesar Cipher shifts every occurrence of a letter by the same amount, the frequency distribution remains unchanged.

An attacker can compare the letter frequencies in the ciphertext with the expected frequencies of English to estimate the correct key.

---

## Why is the Caesar Cipher insecure?

- It has only **26 possible keys**, making exhaustive search almost instantaneous.
- It is vulnerable to **brute-force attacks**.
- It is vulnerable to **frequency analysis** because the statistical distribution of letters is preserved after encryption.
- Modern computers can test every possible key in a fraction of a second.

---

## What I built today

- Implemented a brute-force attack on the Caesar Cipher.
- Tried all 26 possible Caesar shifts automatically.
- Displayed every possible plaintext for the given ciphertext.
- Preserved uppercase letters, lowercase letters, spaces, numbers and punctuation.
- Understood how attackers can break the Caesar Cipher without knowing the secret key.