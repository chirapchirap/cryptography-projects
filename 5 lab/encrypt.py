from func_package import convert_hex_to_bin, wrap_file_code, s_block_1


def encrypt(filename, a, b):
    file_code = read_file_data(filename)
    binary_file_code = list(map(convert_hex_to_bin, file_code))
    wrapped_binary_file_code = wrap_file_code(binary_file_code)
    



def read_file_data(filename):
    file_code = []
    with open(filename, "rb") as file:
        while True:
                byte = file.read(1)
                if not byte:
                        break
                else: 
                        file_code.append(byte)
    return file_code



