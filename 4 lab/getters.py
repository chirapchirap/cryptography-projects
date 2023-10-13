from collections import Counter


def _get_symbol_frequency(text):
    letter_counts = Counter(text)
    most_common_letters = letter_counts.most_common(2)
    return most_common_letters

def _get_key(coefs, mod):
    a = _get_inverse_num_by_mod(coefs[0], mod) % mod
    b = ((-coefs[1]) * a) % mod
    return [a, b]

def _get_inverse_num_by_mod(num, mod):
    for i in range(mod):
        if (num * i) % mod == 1:
            return i
