encoding = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

k = 'осеньосеньосен'
M = 'наступилаосень'

enc = [(encoding.index(i) + encoding.index(j)) % len(encoding)for i, j in zip(k,M)]
print(enc)
enc_str = [encoding[a] for a in enc] 
print(enc_str)