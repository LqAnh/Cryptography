#python file for encrypt and decrypt text file only base on vigenere cipher with size of unicode character
from base64 import (
    b64encode as _b64encode,
    b64decode as _b64decode
)
import time


def _transform(string:str, key:str, mode = "encrypt") -> str:
    key_index:int = 0
    transform_text:str = ""
    
    if type(string) is not str:
        raise TypeError("The input text must be string")
    
    for char in string:
        if mode.startswith("en"):
            transform_text += chr((ord(char)+ord(key[key_index]))%0x110000)
            
            key_index+=1
            
            if key_index == len(key):
                key_index = 0
            
        elif mode.startswith("de"):
            transform_text += chr((ord(char)-ord(key[key_index]))%0x110000)
             
            key_index+=1
          
            if key_index == len(key):
                key_index = 0

        else:
            #print(mode)
            raise TypeError("Not a valid arguement for `mode`")  
        if key_index - 1 == len(key):
            key_index = 0
            
    return transform_text


def para_encrypt(file_path,cipher_key,out_path,base):
    start = time.time()

    with open(file_path,"r") as input_data:
        input_data = input_data.read()
        cipher = encrypt(input_data,cipher_key,base)
    with open(out_path,"w") as output_data:
        output_data.write(cipher)

    end = time.time()
    print(f"Encryption take: {(end-start)*10**3:.03f}ms")



def para_decrypt(file_path,cipher_key,out_path,base):
    start = time.time()

    with open(file_path,"r") as input_data:
        input_data = input_data.read()
        cipher = decrypt(input_data,cipher_key,base)
    with open(out_path,"w") as output_data:
        output_data.write(cipher)

    end = time.time()
    print(f"Decryption take: {(end-start)*10**3:.03f}ms")




def encrypt(plain_text: str, key:str, base64=True) -> str:
    cipher = str(_transform(plain_text, key, mode="encrpyt"))
    
    if base64:
        return _b64encode(cipher.encode()).decode()
    return cipher

def decrypt(cipher: str, key: str, base64=True) -> str:

    if base64:
        cipher = _b64decode(cipher.encode()).decode()
    return str(_transform(cipher, key, mode="decrypt"))



