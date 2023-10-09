# а	 б	в	г	д	е	ж	з	и	й	к	л	м	н	о	п	р	с	т	у	ф	х	ц	ч	ш	щ	ъ	ы	ь	э	ю	я
# 0	 1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31
from count_letters_frequency import _get_symbol_frequency
from affine_cipher_cryptanalysis import _make_cryptoanalysis_affine_cipher

encoding = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я']
]


def __get_symbol_code(symbol):
    for i in range(len(encoding[0]) - 1):
        if symbol == encoding[1][i]:
            return i


encoding_frequent_symbols = ['о', 'е']

text = "бсиьбжгаоялплцкщдцаэглшнокжцкшгезогльнглщишияжржгишкдгибжшксицкщгляябцерлкгэхицкъглскокшгкзихлояигдшазяокэкяжкхс"

text_frequent_symbols = _get_symbol_frequency(text)
for i in range(len(text_frequent_symbols)):
    text_frequent_symbols[i] = text_frequent_symbols[i][0]

mod = len(encoding[0])
print(_make_cryptoanalysis_affine_cipher(text, encoding, mod,
                                         __get_symbol_code(text_frequent_symbols[0]),
                                         __get_symbol_code(text_frequent_symbols[1]),
                                         __get_symbol_code(encoding_frequent_symbols[0]),
                                         __get_symbol_code(encoding_frequent_symbols[1])))
