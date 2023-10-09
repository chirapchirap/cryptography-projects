import sys
from math import gcd as coprime


def _make_cryptoanalysis_affine_cipher(text, encoding, mod,
                                       text_frequent_symbol_code1, text_frequent_symbol_code2,
                                       encoding_frequent_symbol_code1, encoding_frequent_symbol_code2):
    __decrypted_text = ''
    __key = _get_key(mod, text_frequent_symbol_code1, text_frequent_symbol_code2,
                     encoding_frequent_symbol_code1, encoding_frequent_symbol_code2)
    for symbol in text:
        for i in range(len(encoding[0]) - 1):
            if symbol == encoding[1][i]:
                __decrypted_symbol_code = (__key[0] * i + __key[1]) % mod
                __decrypted_symbol = encoding[1][__decrypted_symbol_code]
                __decrypted_text += __decrypted_symbol
                break
    return __decrypted_text


def _get_key(mod, text_frequent_symbol_code1, text_frequent_symbol_code2,
             encoding_frequent_symbol_code1, encoding_frequent_symbol_code2):
    for a in range(mod):
        flag = 0
        for b in range(mod):
            if ((text_frequent_symbol_code1 * a + b) % mod == encoding_frequent_symbol_code1) and ((text_frequent_symbol_code2 * a + b) % mod == encoding_frequent_symbol_code2):
                if coprime(a, mod) == 1:
                    __calculated_a = a
                    __calculated_b = b
                    flag = 1
                    break
        if flag == 1:
            break
    if flag == 0:
        print('Невозможно подобрать ключ для расшифровки')
        sys.exit()
    return [__calculated_a, __calculated_b]


def _get_inverse_num_by_mod(num, mod):
    for i in range(mod):
        if (num * i) % mod == 1:
            return i
