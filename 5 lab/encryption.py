from func_package import convert_hex_to_bin, wrap_file_bits_by_6, make_bin_from_rows_and_cols
from func_package import get_s_block_row_and_column, search_in_s_block, wrap_str_by_8, convert_binary_to_decimal


def encrypt(filename):
    
    file_data = read_file_data(filename)
    binary_file_code = list(map(convert_hex_to_bin, file_data))
    # wrapped_binary_file_code = wrap_file_code(binary_file_code)
    rows_and_cols = list(map(get_s_block_row_and_column,
                         wrap_file_bits_by_6(binary_file_code)))
    rows_and_encrypted_cols = list(map(search_in_s_block, rows_and_cols))
    encrypted_bits = ''.join(
        map(make_bin_from_rows_and_cols, rows_and_encrypted_cols))
    encrypted_bytes = list(map(convert_binary_to_decimal, wrap_str_by_8(encrypted_bits)))
    write_file_data(filename, encrypted_bytes)


def read_file_data(filename):     # Чтение файла
    file_code = []
    with open(filename, "rb") as file:
        while True:
            byte = file.read(1)
            if not byte:
                return file_code
            else:
                file_code.append(byte)

def write_file_data(filename, data):
    with open(filename, "wb") as file:
            file.write(bytes(data))
