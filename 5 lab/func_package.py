from textwrap import wrap
from main import a, b

s_block_1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

def convert_hex_to_bin(x):
        return bin(ord(x))[2:].zfill(8)

def wrap_file_code(code):
        wrapped_code = wrap(code, 6)
        if wrapped_code[-1] < 6:
                wrapped_code[-1] = wrapped_code[-1].zfill(6)
        return wrapped_code

        
