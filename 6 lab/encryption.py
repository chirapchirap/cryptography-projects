from func_package import use_feistel_cipher_for_encryption    


def encrypt(filename): 
    file_code = read_file_data(filename)
    encrypted_file_code = list(map(use_feistel_cipher_for_encryption, file_code))
    write_file_data(filename, encrypted_file_code)


def read_file_data(filename):     # Чтение файла
    with open(filename, "rb") as file:
        file_code = file.read()
        return list(file_code)
    
    
def write_file_data(filename, data):    # Запись в файл 
    with open(filename, "wb") as file:
        file.write(bytes(data))


