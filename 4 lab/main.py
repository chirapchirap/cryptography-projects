# а	 б	в	г	д	е	ж	з	и	й	к	л	м	н	о	п	р	с	т	у	ф	х	ц	ч	ш	щ	ъ	ы	ь	э	ю	я
# 0	 1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31
from getters import _get_symbol_frequency, _get_key
from affine_cipher_cryptanalysis import _make_cryptoanalysis_affine_cipher

# Наша кодировка
encoding = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31],
    ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
]

# Функция получения кода символа по указанной кодировке
def __get_symbol_code(symbol):
    for i in range(len(encoding[0]) - 1):
        if symbol == encoding[1][i]:
            return i

# Часто встречающиеся буквы в алфавите(кодировке)
encoding_frequent_symbols = ['о', 'н']

text = "бсиьбжгаоялплцкщдцаэглшнокжцкшгезогльнглщишияжржгишкдгибжшксицкщгляябцерлкгэхицкъглскокшгкзихлояигдшазяокэкяжкхс"

# Вызывается функция, которая возвращает 2 часто встречающиеся буквы в зашифрованном тексте
text_frequent_symbols = _get_symbol_frequency(text)

for i in range(len(text_frequent_symbols)):
    text_frequent_symbols[i] = text_frequent_symbols[i][0]

mod = len(encoding[0])

print(f"* Зашифрованный текст: {text}")
print(f"* Часто встречаемые буквы = {text_frequent_symbols}")

# Вызывается функция, в которой выполняется криптоанализ аффинного шифра. Эта функция принимает аргументы: зашифрованный текст, кодировка, модуль и коды букв(2-ух часто встречающихся в тексте и в алфавите) с учетом нашей кодировки)
# Функция возвращает массив: В 0 ячейчке лежит текст, расшифрованный по предположению
#                            В 1 лежит альфа и бета, найденное по предположению
result_of_cryptoanalysis = _make_cryptoanalysis_affine_cipher(text, encoding, mod,
                                                              __get_symbol_code(text_frequent_symbols[0]),
                                                              __get_symbol_code(text_frequent_symbols[1]),
                                                              __get_symbol_code(encoding_frequent_symbols[0]),
                                                              __get_symbol_code(encoding_frequent_symbols[1]))

print(f"* Ek({text_frequent_symbols[0]}) = {encoding_frequent_symbols[0]}; Ek({text_frequent_symbols[1]}) = {encoding_frequent_symbols[1]}:\n  Расшифрованный текст(по предположению) = {result_of_cryptoanalysis[0]}")
encryption_key = _get_key(result_of_cryptoanalysis[1], mod)
print(f"* Ключ для шифрования(для 1 предположения): [a, b] = {encryption_key}")

result_of_cryptoanalysis = _make_cryptoanalysis_affine_cipher(text, encoding, mod,
                                                              __get_symbol_code(text_frequent_symbols[0]),
                                                              __get_symbol_code(text_frequent_symbols[1]),
                                                              __get_symbol_code(encoding_frequent_symbols[1]),
                                                              __get_symbol_code(encoding_frequent_symbols[0]))
print(f"* Ek({text_frequent_symbols[0]}) = {encoding_frequent_symbols[1]}; Ek({text_frequent_symbols[1]}) = {encoding_frequent_symbols[0]}:\n  Расшифрованный текст(по предположению) = {result_of_cryptoanalysis[0]}")

encryption_key = _get_key(result_of_cryptoanalysis[1], mod)
print(f"* Ключ для шифрования(для второго предположения): [a, b] = {encryption_key}")
