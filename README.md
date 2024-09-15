Playfair Cipher Encryption/Decryption Program

This Python program implements the Playfair Cipher, a manual symmetric encryption technique, which uses a 5x5 grid of letters to encrypt or decrypt a message. The cipher pairs each letter in the plaintext with another and transforms it into ciphertext using specific rules based on the positions of the characters in the grid.
Features

    Encrypt plaintext using the Playfair cipher.
    Decrypt ciphertext using the Playfair cipher.
    Generates a 5x5 grid based on a key.
    Handles padding for duplicate characters in plaintext.
    Allows user to input their own key and plaintext/ciphertext.

Prerequisites

You need Python installed to run this program.
How It Works
1. Grid Creation

    The grid is created using a keyword provided by the user.
    The program removes any repeated letters in the key and fills the rest of the grid with the remaining letters of the alphabet.
    The letter "i" and "j" are considered the same in this implementation.

2. Encryption/Decryption

    The encryption and decryption processes are handled by separating the input text into pairs of characters.
    Depending on their positions in the grid, the program performs one of the following transformations:
        Box Case: If the characters form a rectangle, they are swapped along the diagonal.
        Column Case: If the characters are in the same column, they are shifted downwards (encryption) or upwards (decryption).
        Row Case: If the characters are in the same row, they are shifted to the right (encryption) or to the left (decryption).

3. Padding

    For encryption, padding is automatically added if two consecutive letters are the same. For example, "xx" would be padded to "xq" or "qx".
    During decryption, the program removes padding that was added during encryption.

Functions Overview

    print_stylized_text(): Prints a stylized banner.
    print_grid(matrix): Displays the 5x5 grid matrix.
    create_grid(key): Generates the 5x5 grid matrix based on the key.
    box_case(), column_case(), row_case(): Handle different Playfair cipher cases.
    padding_case(): Adds necessary padding for encryption and handles removing padding during decryption.
    encrypt(): Encrypts a pair of characters using the Playfair cipher.
    decrypt(): Decrypts a pair of characters using the Playfair cipher.
    find_in_matrix(): Finds the row and column of a character in the grid.
    start_encryption(): Initiates the encryption process.
    start_decryption(): Initiates the decryption process.
    revert_j(): Reverts any "j" in the text back to "i" after decryption.

Usage

    Encryption:
        Run the program and enter a key for encryption when prompted.
        Input the plaintext message.
        The program will output the corresponding ciphertext.

    Decryption:
        Run the program and enter the same key used for encryption.
        Input the ciphertext message.
        The program will output the original plaintext message.

Example

bash

Enter key for encryption:
playfair
    +---------------------------+
    |        GRID MATRIX        |
    +---------------------------+
    | ['p', 'l', 'a', 'y', 'f'] |
    | ['i', 'r', 'b', 'c', 'd'] |
    | ['e', 'g', 'h', 'k', 'm'] |
    | ['n', 'o', 'q', 's', 't'] |
    | ['u', 'v', 'w', 'x', 'z'] |
    +---------------------------+
    |         Playfair          |
    +---------------------------+

Enter text you want to encrypt:
hello
Ciphertext: kcqls
