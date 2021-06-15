'''
    caesar_decrypt.py
    given key and caesar ciphertext translate into plaintext 
'''
import string, sys

def decrypt(key, ciphertext):
    ''' 
        params: char key - offset of A
                string ciphertext - encoded message to be read
        desc: decrypt message by reversing offset of each letter by key
    '''
    shift = ord(key.upper()) - 65
    plaintext = ""
    for c in ciphertext.upper():
        if ord(c) != ord(" "):
            nchar = chr(ord(c) - shift)
            if ord(nchar) < 65:
                nchar = chr(ord(nchar) + 26)
            elif ord(nchar) > 90:
                nchar = chr(ord(nchar) - 26)
            plaintext += nchar
        else:
            plaintext += " "
    return plaintext

if __name__ == "__main__":
    try:
        # automatic mode: get key and ciphertext from commandline options
        key = sys.argv[1]
        ciphertext = sys.argv[2]
    except:
        # interactive mode: prompt user
        key = input("Key (char); 'A'= ")
        ciphertext = inpt("Ciphertext: ")
    plaintext = decrypt(key, ciphertext)
    print(plaintext)

