# Crypto Nite - Day 8

## Topics Covered

* Introduction to Columnar Transposition Cipher
* Keyword-based Column Ordering
* Encryption Process
* Decryption Process
* Padding
* Time Complexity
* Advantages
* Limitations

---

## What is a Columnar Transposition Cipher?

The **Columnar Transposition Cipher** is a **classical transposition cipher** that encrypts messages by **rearranging the positions of characters** according to a secret keyword.

Unlike substitution ciphers, the characters themselves are **never changed**. Instead, the plaintext is written into a matrix row by row, and the columns are read in an order determined by the keyword.

Since only the positions of the characters change, the ciphertext contains exactly the same letters as the plaintext, but in a different order.

---

## Keyword-based Column Ordering

The secret key is a **keyword**.

Each letter of the keyword is assigned a number based on its alphabetical order.

For example,

```
Keyword : Z E B R A
```

Arrange the letters alphabetically.

```
A B E R Z
```

Assign numbers.

```
A → 1
B → 2
E → 3
R → 4
Z → 5
```

Write these numbers below the original keyword.

```
Z E B R A
5 3 2 4 1
```

These numbers determine the order in which the columns are read during encryption.

---

## Encryption Process

Encryption consists of six simple steps.

### Step 1

Choose a keyword.

Example:

```
Keyword = ZEBRA
```

---

### Step 2

Remove spaces from the plaintext if required.

Example:

```
ATTACKATDAWN
```

---

### Step 3

Write the plaintext row by row beneath the keyword.

```
Z   E   B   R   A
5   3   2   4   1
-----------------
A   T   T   A   C
K   A   T   D   A
W   N
```

---

### Step 4

If the final row is incomplete, pad the remaining cells.

Example:

```
Z   E   B   R   A
5   3   2   4   1
-----------------
A   T   T   A   C
K   A   T   D   A
W   N   X   X   X
```

---

### Step 5

Read the columns according to the keyword numbering.

```
Column 1 → A → CAX
Column 2 → B → TTX
Column 3 → E → TAN
Column 4 → R → ADX
Column 5 → Z → AKW
```

---

### Step 6

Concatenate the columns.

```
CAXTTXTANADXAKW
```

This is the ciphertext.

---

## Decryption Process

Decryption reverses the encryption process.

Instead of filling the matrix row by row, the columns are reconstructed first.

The process consists of five steps.

### Step 1

Determine the number of rows and columns.

The number of columns equals the length of the keyword.

The number of rows is

```
Rows = Ciphertext Length ÷ Number of Columns
```

---

### Step 2

Create an empty matrix of the required size.

---

### Step 3

Fill each column according to the keyword numbering using the ciphertext.

For example,

```
Ciphertext:

CAXTTXTANADXAKW
```

produces

```
Z   E   B   R   A
5   3   2   4   1
-----------------
A   T   T   A   C
K   A   T   D   A
W   N   X   X   X
```

---

### Step 4

Read the matrix row by row.

```
ATTACKATDAWNXXX
```

---

### Step 5

Remove the padding characters.

Recovered plaintext:

```
ATTACKATDAWN
```

---

## Padding

If the plaintext does not completely fill the matrix, additional characters are added.

Common padding characters include

```
X
```

or

```
Z
```

Padding ensures that every row contains the same number of columns, making both encryption and decryption straightforward.

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

* More secure than the Rail Fence Cipher due to the use of a secret keyword.
* Rearranges character positions without modifying the characters themselves.
* Simple to understand and implement.
* Uses a key to determine the column reading order.
* Runs in linear time.

---

## Limitations

* Preserves the original letter frequencies.
* Vulnerable to frequency analysis and known-plaintext attacks.
* Short keywords provide limited security.
* Not considered secure by modern cryptographic standards.

---

## Key Takeaways

* Columnar Transposition is a **transposition cipher**, not a substitution cipher.
* Characters are never modified; only their positions are rearranged.
* The keyword determines the order in which columns are read.
* Encryption writes the plaintext row by row and reads the columns according to the keyword.
* Decryption fills the columns according to the keyword and then reads the matrix row by row.
* Padding is often used to create a complete rectangular matrix.
* Although stronger than the Rail Fence Cipher, Columnar Transposition is still vulnerable to modern cryptographic attacks.