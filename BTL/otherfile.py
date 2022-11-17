#python file for encrypt and decrypt any file only base on vigenere cipher with size of 256 bit.

import time
def encrypt(in_filepath,cipher_key,out_filepath):
    
    start = time.time()

    with open(in_filepath, "rb") as image:
        
        key_index:int = 0
        f = image.read()
        b = bytearray(f)

        test = []
        for i in b:
            test.append((i + ord(cipher_key[key_index]))%256)
            key_index+=1
            if key_index == len(cipher_key):
                key_index = 0
        with open(out_filepath, "wb") as encrypted:
            encrypted.write(bytearray(test))


    end = time.time()

    print(f"Encryption take: {(end-start)*10**3:.03f}ms")



def decrypt(in_filepath,cipher_key,out_filepath):
        
    start = time.time()

    with open(in_filepath, "rb") as image:
        
        key_index:int = 0
        f = image.read()
        b = bytearray(f)

        test = []
        for i in b:
            test.append((i - ord(cipher_key[key_index]))%256)
            key_index+=1
            if key_index == len(cipher_key):
                key_index = 0
        with open(out_filepath, "wb") as decrypted:
            decrypted.write(bytearray(test))


    end = time.time()

    print(f"Decryption take: {(end-start)*10**3:.03f}ms")