def encrypt(filename, key):
    file_data = read_file_data(filename)
    encrypted_data = []
    for byte_array in file_data:
        if len(byte_array) == 6:
            for i in range(6):
                temp_byte = byte_array[key[0][i]-1]
                byte_array[key[0][i]-1] = byte_array[key[1][i]-1]
                byte_array[key[1][i]-1] = temp_byte
        else:
            for i in range(len(byte_array) - 1):
                temp_byte = byte_array[key[0][i]-1]
                byte_array[key[0][i]-1] = byte_array[key[1][i]-1]
                byte_array[key[1][i]-1] = temp_byte
        encrypted_data.append(byte_array)
    write_file_data(filename, encrypted_data)


def read_file_data(filename):
    data_list = []
    with open(filename, "rb") as file:
        while True:
            byte_chunk = file.read(6)
            if not byte_chunk:
                break
            data_list.append(bytearray(byte_chunk))
    return data_list


def write_file_data(filename, encrypted_data):
    with open(filename, "wb") as file:
        for byte_array in encrypted_data:
            file.write(byte_array)
