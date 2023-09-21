from math import gcd as coprime


def encrypt(filename, a, b, mod):
    file_data = read_file_data(filename)
    encrypted_data = ""
    if coprime(a, mod) == 1:
        for i in range(len(file_data)):
            num = a * file_data[i] + b
            if num > mod:
                num = num % mod
            temp_num_chr = chr(num)
            encrypted_data += temp_num_chr
    write_file_data(filename, encrypted_data)


def write_file_data(filename, encrypted_data):
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def read_file_data(filename):
    with open(filename, 'rb') as file:
        return file.read()
