from cryptography.fernet import Fernet

file = r"C:\Users\User\OneDrive\Рабочий стол\1.png"
key = Fernet.generate_key()





def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)



