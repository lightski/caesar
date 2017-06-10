'''
    caesar_decrypt.py
    given key and caesar ciphertext translate into plaintext 
'''
import string, sys

def decrypt(key, ciphertext):
    ''' 
        params: int key - offset of A
                string ciphertext - encoded message to be read
        desc: decrypt message by reversing offset of each letter by key
    '''
    shift = ord(key.upper()) - 65
    plaintext = ""
    for c in (ciphertext.replace(" ","")).upper():
#        print("cipher char is:",c)
        nchar = chr(ord(c) - shift)
        if ord(nchar) < 65:
            nchar = chr(ord(nchar) + 26)
        elif ord(nchar) > 90:
            nchar = chr(ord(nchar) - 26)
        plaintext += nchar
#        print("converting to:",nchar)
    return plaintext

if __name__ == "__main__":
    try:
        # automatic mode: get key and ciphertext from commandline options
        key = sys.argv[1]
        ciphertext = sys.argv[2]
    except:
        # interactive mode: prompt user
        key = input("Key/offset (char); 'A'= ")
        ciphertext = input("Ciphertext: ")
    plaintext = decrypt(key, ciphertext)
    #print(' '.join(plaintext[i:i+5] for i in range(0,len(plaintext),5)))
    # maybe someday guess at spacing. for now just print raw
    print(plaintext)

