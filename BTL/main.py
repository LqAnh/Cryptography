import os
import vigenere as vig
import otherfile as of

list_text_file = []
list_other_file = []

file_path = "./disk/"
encrypt_path="./encrypt/"
decrypt_path="./decrypt/"

cipher_key="LãquỐc anh"

def checkFileInDir(file_path):
    for filename in os.listdir(file_path):
        if filename.startswith("."): 
            continue

        elif filename.endswith(".txt"):
            list_text_file.append(filename) 

        else:
            list_other_file.append(filename)

def encrypt():
    
    checkFileInDir(file_path)
    
    for file in list_text_file:
        vig.para_encrypt(file_path+file,cipher_key,encrypt_path+"en_"+file,base=True)
    list_text_file.clear()

    for file in list_other_file:
        of.encrypt(file_path+file,cipher_key,encrypt_path+"en_"+file)
    list_other_file.clear()

def decrypt():
    checkFileInDir(encrypt_path)
    
    for file in list_text_file:
        vig.para_decrypt(encrypt_path+file,cipher_key,decrypt_path+"de_"+file,base=True)
    list_text_file.clear()

    for file in list_other_file:
        of.decrypt(encrypt_path+file,cipher_key,decrypt_path+"de_"+file)
    list_other_file.clear()

encrypt()
decrypt()