from math import gcd as coprime


def decrypt(filename, a, b, mod):
    gcd, x, y = get_inverse_num(a, mod)
    if gcd == 1:
        inverse_num = (x % mod + mod) % mod
    else:
        inverse_num = -1

    file_data = read_file_data(filename)
    decrypted_data = []
    if coprime(a, mod) == 1:

        for byte in file_data:
            if byte > b:
                decrypted_byte = ((byte - b) * inverse_num) % mod 
            else: 
                decrypted_byte = ((byte - b + mod) % mod) * inverse_num % mod
            decrypted_data.append(decrypted_byte)
        write_file_data(filename, decrypted_data)


def get_inverse_num(a, mod):
    if a == 0:
        return mod, 0, 1
    gcd, x1, y1 = get_inverse_num(mod % a, a)
    x = y1 - (mod//a) * x1
    y = x1
    return gcd, x, y


def write_file_data(filename, decrypted_data):
    with open(filename, 'wb') as file:
        file.write(bytes(decrypted_data))


def read_file_data(filename):
    with open(filename, 'rb') as file:
        return file.read()
