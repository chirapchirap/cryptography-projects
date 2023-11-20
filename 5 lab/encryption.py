from func_package import convert_hex_to_bin, wrap_file_code, s_block_1, get_s_block_row_and_column


def encrypt(filename):
    file_code = read_file_data(filename)
    binary_file_code = list(map(convert_hex_to_bin, file_code))
    # wrapped_binary_file_code = wrap_file_code(binary_file_code)
    rows_and_columns = list(map(get_s_block_row_and_column, wrap_file_code(binary_file_code)))


def read_file_data(filename):
    file_code = []
    with open(filename, "rb") as file:
        while True:
            byte = file.read(1)
            if not byte:
                return file_code
            else:
                file_code.append(byte)
