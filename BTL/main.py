import os
import vigenere as vig
import otherfile as of

list_text_file = []
list_other_file = []

cipher_key="LãquỐc anh"

encrypt_path="./encrypt/"
decrypt_path="./decrypt/"

def checkFileInDir(file_path):
    for filename in os.listdir(file_path):
        if filename.startswith("."): 
            continue

        elif filename.endswith(".txt"):
            list_text_file.append(filename) 

        else:
            list_other_file.append(filename)

def encrypt():
    file_path = "./disk/"
    checkFileInDir(file_path)
    
    for file in list_text_file:
        vig.encryptv2(file_path+file,cipher_key,encrypt_path+"en_"+file,base=True)
    list_text_file.clear()

    for file in list_other_file:
        of.encrypt(file_path+file,cipher_key,encrypt_path+"en_"+file)
    list_other_file.clear()

def decrypt():
    checkFileInDir(encrypt_path)
    
    for file in list_text_file:
        vig.decryptv2(encrypt_path+file,cipher_key,decrypt_path+"de_"+file,base=True)
    list_text_file.clear()

    for file in list_other_file:
        of.decrypt(encrypt_path+file,cipher_key,decrypt_path+"de_"+file)
    list_other_file.clear()

encrypt()
decrypt()