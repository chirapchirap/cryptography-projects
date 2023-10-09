from collections import Counter


def _get_symbol_frequency(text):
    letter_counts = Counter(text)
    most_common_letters = letter_counts.most_common(2)
    return most_common_letters
