import os
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_file(key, file_path):
    cipher_suite = Fernet(key)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    encrypted_file_path = file_path + '.encrypted'

    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    return encrypted_file_path

def decrypt_file(key, encrypted_file_path):
    cipher_suite = Fernet(key)

    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    decrypted_file_path = encrypted_file_path.replace('.encrypted', '.decrypted')

    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path

if __name__ == "__main__":
    key = generate_key()
    key_filename = "encryption_key.key"
    save_key(key, key_filename)

    directory_path = "path_to_your_directory"
    
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            encrypted_file_path = encrypt_file(key, file_path)
            print(f"Encrypted {filename} to {encrypted_file_path}")

    for filename in os.listdir(directory_path):
        if filename.endswith('.encrypted'):
            encrypted_file_path = os.path.join(directory_path, filename)
            decrypted_file_path = decrypt_file(key, encrypted_file_path)
            print(f"Decrypted {filename} to {decrypted_file_path}")