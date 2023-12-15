encoding = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

msg = 'сткджфхщвуфпкмвоуртждпрдвпкл'
i = 0
while i < 32:
    print('k = ' + str(i) + ':', [(encoding.index(let) - i) % len(encoding) for let in msg])
    print(''.join([encoding[(encoding.index(let) - i) % len(encoding)] for let in msg]))
    i += 1
else: print('Конец')





