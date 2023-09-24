from math import gcd as coprime


def encrypt(filename, a, b, mod):
    file_data = read_file_data(filename)
    encrypted_data = []
    if coprime(a, mod) == 1:
        for byte in file_data:
            encrypted_byte = a * byte + b
            if encrypted_byte > mod:
                encrypted_byte = encrypted_byte % mod
            encrypted_data.append(encrypted_byte)
    write_file_data(filename, encrypted_data)


def write_file_data(filename, encrypted_data):
    with open(filename, 'wb') as file:
        file.write(bytes(encrypted_data))


def read_file_data(filename):
    with open(filename, 'rb') as file:
        return file.read()
