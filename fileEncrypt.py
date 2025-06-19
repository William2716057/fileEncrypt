from cryptography.fernet import Fernet
import sys
import os


#generate key
def generate_key(key_file='secret.key'):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)
    print(f"Key saved to {key_file}")
    return key
    
key = generate_key()
    
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted)
        
    print(f"Encrypted file saved as {file_path}.enc")
    
key = generate_key()
encrypt_file('secret.txt', key)
    
