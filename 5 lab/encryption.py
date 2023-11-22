from func_package import convert_hex_to_bin, wrap_file_bits_by_6, make_bin_from_rows_and_cols
from func_package import get_s_block_row_and_column, get_row_and_value, wrap_str_by_8, convert_binary_to_decimal


def encrypt(filename):
    wrapped_bits_seq = wrap_file_bits_by_6(''.join(map(convert_hex_to_bin, read_file_data(filename))))
    popped_data = wrapped_bits_seq.pop() if len(wrapped_bits_seq[-1]) < 6 else ''
    write_file_data(filename, list(
        map(convert_binary_to_decimal, wrap_str_by_8(''.join(map(make_bin_from_rows_and_cols,
            map(get_row_and_value, map(get_s_block_row_and_column, wrapped_bits_seq))))+popped_data))))


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
