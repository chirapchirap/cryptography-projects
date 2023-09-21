from math import gcd as coprime


def decrypt(filename, a, b, mod):

    gcd, x, y = get_inverse_num(a, mod)
    if gcd == 1:
        inverse_num = (x % mod + mod) % mod
    else:
        inverse_num = -1

    file_data = read_file_data(filename)
    temp_file_data_chr = file_data.decode('utf-8')
    decrypted_data = ""
    if coprime(a, mod) == 1:
        #print(len(file_data))
        #print(len(temp_file_data_chr))
        #for i in range(len(file_data)):
        for i in range(len(temp_file_data_chr)):
            #num = inverse_num * (file_data[i]- b)
            num = inverse_num * (ord(temp_file_data_chr[i])- b)
            while num < 0:
                num += mod
            if num > mod:
                num = num % mod
            temp_num_chr = chr(num)
            decrypted_data += temp_num_chr
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
        file.write(decrypted_data.encode('utf-8'))


def read_file_data(filename):
    with open(filename, 'rb') as file:
        return file.read()
