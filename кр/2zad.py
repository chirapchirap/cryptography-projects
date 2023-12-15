a, b = 2, 4
alpha, beta = 17, 31
encoding = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
open_msg = 'аффинныйшифр'
dec_msg = 'дммхяяьчфхме'
enc_codes = [(encoding.index(let) * a + b) % len(encoding) for let in open_msg]
enc_letters = [encoding[code] for code in enc_codes]
print(enc_codes, enc_letters)

dec_codes = [(alpha *(encoding.index(let) - b)) % len(encoding) for let in dec_msg]
dec_letters = [encoding[code] for code in dec_codes]
print(dec_codes, dec_letters)



