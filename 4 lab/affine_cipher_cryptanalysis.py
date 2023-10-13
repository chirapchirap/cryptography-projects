import sys
from math import gcd as coprime
from getters import _get_key


def _make_cryptoanalysis_affine_cipher(text, encoding, mod,
                                       text_frequent_symbol_code1, text_frequent_symbol_code2,
                                       encoding_frequent_symbol_code1, encoding_frequent_symbol_code2):
    __decrypted_text = ''
    __assumption_coefficients = _get_assumption_alpha_and_beta(mod, text_frequent_symbol_code1, text_frequent_symbol_code2,    # Вызывается функция, которая находит альфа и бета 
                                                               encoding_frequent_symbol_code1, encoding_frequent_symbol_code2) # из системы уравнений, являющихся предположением 
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
    
    key = _get_key(__assumption_coefficients, mod)
    return __decrypted_text, key

def _get_assumption_alpha_and_beta(mod, text_frequent_symbol_code1, text_frequent_symbol_code2,         # Функция, которая решает систему уравнений и находит афльфа и бета
                                   encoding_frequent_symbol_code1, encoding_frequent_symbol_code2):     # Если система уравнений не решается, то возращает -1, которое дальше 
    for alpha in range(mod):                                                                            # обрабатывается
        if coprime(alpha, mod) != 1:
            continue
        for beta in range(mod):
            if ((text_frequent_symbol_code1 * alpha + beta) % mod == encoding_frequent_symbol_code1) and (
                    (text_frequent_symbol_code2 * alpha + beta) % mod == encoding_frequent_symbol_code2):
                return [alpha, beta]
    return [-1]




