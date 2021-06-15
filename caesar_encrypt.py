'''
    caesar_encrypt.py
    given key, encrypt plaintext into caesar ciphertext
'''
import string, sys

def encrypt(key, plaintext):
    ''' 
        params: char key - offset of A
                string plaintext - message to be encoded
        desc: encrypt message by offsetting each letter by key
    '''
    shift = ord(key.upper()) - 65
    ciphertext = ""
    for c in plaintext.upper():
        if ord(c) != ord(" "):
            nchar = chr(ord(c) + shift)
            if ord(nchar) > 90:
                nchar = chr(ord(nchar) - 26)
            ciphertext += nchar
        else:
            ciphertext += " "
    return ciphertext

if __name__ == "__main__":
    try:
        # automatic mode: get key and plaintext from commandline options
        key = sys.argv[1]
        plaintext = sys.argv[2]
    except:
        # interactive mode: prompt user
        key = input("Key (char); 'A'= ")
        plaintext = input("Plaintext: ")
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

