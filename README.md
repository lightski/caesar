# Caesar Cipher

## Quickstart

Encrypt, decrypt, and break Caesar's cipher! Requires python3.

Run interactively like this:
```
    python3 caesar_encrypt.py
    python3 caesar_decrypt.py
    python3 caesar_break.py
```

Alternatively, provide key and text to encrypt, or just text to break, as command line option.

## Description

Project to mess around with the Caesar cipher. Caesar's cipher is simple character replacement. Pick a letter (other than A) then shift all the characters such that every plaintext A is ciphertext your chosen letter, every B becomes the letter after, C the letter after that, and so on. Caesar's cipher is classic example of a very weak encryption. It is vulnerable to frequency analysis among other things. The most common letter in English is 'E'. So, in this project, we break Caesar ciphers by examining the ciphertext. Letters with frequency of 10% or greater could be 'E' in the plaintext; after identifying the possibilities, we decrypt and discover the plaintext.

NOTE: since Caesar keyspace is so small, brute-force attacks are trivial to launch and 100% effective. In case of small ciphertext this may be the only possible attack, so for ease of use `caesar_break.py` has the option to run bruteforce as well.

The project has three files:

1. caesar\_encrypt.py encrypts some plaintext into a caesar ciphertext. It consists of an encrypt() function and a wrapper.
1. caesar\_decrypt.py decrypts some caesar ciphertext back into plaintext. It consists of a decrypt() function and a wrapper.
2. caesar\_break.py applies frequency analysis to given caesar ciphertext. It uses decrypt() from caesar\_decrypt.py


