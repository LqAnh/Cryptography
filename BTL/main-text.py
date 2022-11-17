import vigenere as vig
import os

list_text_file = []
list_other_file = []

file_path="./disk/"
encrypt_path="./encrypt-text/"
decrypt_path="./decrypt-text/"

cipher_key="LãquỐc anh"

def checkFileInDir(file_path):
    for filename in os.listdir(file_path):
        if filename.endswith(".txt"): 
            list_text_file.append(filename) 

        else:
            continue

def encrypt():
    checkFileInDir(file_path)
    for file in list_text_file:
        vig.encryptv2(file_path+file,cipher_key,encrypt_path+"en_"+file,False)
    list_text_file.clear()

def decrypt():
    checkFileInDir(encrypt_path)
    for file in list_text_file:
        vig.decryptv2(encrypt_path+file,cipher_key,decrypt_path+"de_"+file,False)
    list_text_file.clear()

encrypt()
decrypt()