**vigenere.py: python code to implement vigenere cipher in unicode with space of 1,114,112.**

**otherfile.py: python code to implement vigenere cipher for any file with space of 256.**

    note: the program can only run with small file because it need to load the file into ram to process. If the file is too large the program might be lag

**main.py**: main program for all type of file, of course it contains text file program bellow

**main-text.py**: main program for only text file 

you need to fill in these 2 files some paremeters bellow:

* `file_path`: location of the original folder contains the file to encrypt
* `encrypt_path`: location for encrypted file to write out by encrypt function and also location to read by the decrypt function

* `decrypt_path`: location for decrypted file to write out by decrypt function
* `cipher_key`: key to encrypt, decrypt

`./disk`: location of original file also `file_path` parameter

> **you need to create these bellow folder to run two main program**
>
> ---
>
>

`./encrypt`: location of encrypted file by `main.py` also `encrypt_path` location

`./decrypt`: location of decrypted file by `main.py` also `decrypt_path` location

`./encrypt-text`: location of encrypted file by `main-text.py` also `encrypt_path` location

`./decrypt-text`: location of decrypted file by `main-text.py` also `d		ecrypt_path` location
