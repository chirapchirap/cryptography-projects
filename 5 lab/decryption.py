from func_package import convert_hex_to_bin, wrap_file_bits_by_6, make_bin_from_rows_and_cols, get_row_and_col_index
from func_package import get_s_block_row_and_column, get_row_and_value, wrap_str_by_8, convert_binary_to_decimal


def decrypt(filename):
    file_data = read_file_data(filename)
    binary_file_code = list(map(convert_hex_to_bin, file_data))
    bits_seq = ''.join(binary_file_code)
    wrapped_bits_seq = wrap_file_bits_by_6(bits_seq)
    popped_data = wrapped_bits_seq.pop() if len(wrapped_bits_seq[-1]) < 6 else ''
    rows_and_cols = list(map(get_s_block_row_and_column, wrapped_bits_seq))
    rows_and_decrypted_cols = list(map(get_row_and_col_index, rows_and_cols))
    encrypted_bits = ''.join(map(make_bin_from_rows_and_cols, rows_and_decrypted_cols))
    encrypted_bytes = list(map(convert_binary_to_decimal, wrap_str_by_8(encrypted_bits+popped_data)))
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


def write_file_data(filename, data):  # запись в файл
    with open(filename, "wb") as file:
        file.write(bytes(data))
