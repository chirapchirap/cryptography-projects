from textwrap import wrap
import chardet

a, b = 2, 5

s_block_1 = tuple([
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
])


def convert_hex_to_bin(x):  # non-ascii символы в бинарный вид
    return bin(ord(x))[2:].zfill(8)


def convert_int_to_bin(x):  # число в бинарный вид
    return int(x, 2)


def wrap_file_bits_by_6(bits):  # разбиение последовательности битов по 6
    wrapped_code = wrap(
        ''.join([value for index, value in enumerate(bits)]), 6)
    if len(wrapped_code[-1]) < 6:
        wrapped_code[-1] = wrapped_code[-1].zfill(6)
    return wrapped_code

def wrap_str_by_8(bits): # разбиение последовательности битов по 8
    wrapped_code = wrap(bits, 8)
    if len(wrapped_code[-1]) < 6:
        wrapped_code[-1] = wrapped_code[-1].zfill(6)
    return wrapped_code

def convert_binary_to_decimal(x): # бинарный в десятичный 
    return int(x, 2)


def get_s_block_row_and_column(x):  # получение строки и столбца из 6 бит
    row = int(
        ''.join([value for index, value in enumerate(x) if index in (a-1, b-1)]), 2)
    column = int(
        ''.join([value for index, value in enumerate(x) if index not in (a-1, b-1)]), 2)
    return [row, column]


def search_in_s_block(pos):  # поиск значения в блоке
    return [pos[0], s_block_1[pos[0]][pos[1]]]


def make_bin_from_rows_and_cols(pos):  # замена координат в s_блоке в бинарном виде
    bin_row = bin(pos[0])[2:].zfill(2)
    bin_col = bin(pos[1])[2:].zfill(4)
    bits_seq = ['0']*6
    row = (value for index, value in enumerate(bin_row))
    col = (value for index, value in enumerate(bin_col))
    for index, value in enumerate(bits_seq):
        if index in (a-1, b-1):
            bits_seq[index] = str(next(row))
        else:
            bits_seq[index] = str(next(col))
    return ''.join(bits_seq)

def get_file_encoding(filename): # получение кодировки файла
    rawdata = open(filename, 'rb').read()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    return charenc
