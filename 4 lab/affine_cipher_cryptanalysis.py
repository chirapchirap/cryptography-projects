import sys
from math import gcd as coprime


def _make_cryptoanalysis_affine_cipher(text, encoding, mod,
                                       text_frequent_symbol_code1, text_frequent_symbol_code2,
                                       encoding_frequent_symbol_code1, encoding_frequent_symbol_code2):
    __decrypted_text = ''
    __assumption_coefficients = _get_assumption_alpha_and_beta(mod, text_frequent_symbol_code1, text_frequent_symbol_code2,
                                                               encoding_frequent_symbol_code1, encoding_frequent_symbol_code2)
    if __assumption_coefficients[0] == -1:
        return 'Невозможно подобрать alpha и beta'
    for symbol in text:
        for i in range(len(encoding[0])):
            if symbol == encoding[1][i]:
                __decrypted_symbol_code = (
                    __assumption_coefficients[0] * i + __assumption_coefficients[1]) % mod
                __decrypted_symbol = encoding[1][__decrypted_symbol_code]
                __decrypted_text += __decrypted_symbol
                break
    
    #key = __get_key(__assumption_coefficients)
    return __decrypted_text


def _get_assumption_alpha_and_beta(mod, text_frequent_symbol_code1, text_frequent_symbol_code2,
                                   encoding_frequent_symbol_code1, encoding_frequent_symbol_code2):
    for alpha in range(mod):
        if coprime(alpha, mod) != 1:
            continue
        for beta in range(mod):
            if ((text_frequent_symbol_code1 * alpha + beta) % mod == encoding_frequent_symbol_code1) and (
                    (text_frequent_symbol_code2 * alpha + beta) % mod == encoding_frequent_symbol_code2):
                return [alpha, beta]
    #print('Невозможно подобрать ключ для расшифровки')
    return [-1]


def _get_inverse_num_by_mod(num, mod):
    for i in range(mod):
        if (num * i) % mod == 1:
            return i

def __get_key(coefs, mod):
    a = _get_inverse_num_by_mod(coefs[0], mod) % mod
    b = ((-coefs[1]) * a) % mod
    return [a, b]
