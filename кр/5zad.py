encoding = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

plain = 'шифрвиженера'
enc =   'ьизтвъиепедв'
mod = len(encoding)
key = []

def foo(x):
    for index, value in enumerate(encoding):
        if (encoding.index(x[0]) + index) % mod == encoding.index(x[1]):
            return index

    return [x[0], x[1]] 

res = list(map(foo, zip(plain, enc)))
res_str = [encoding[let] for let in res]
print(res)
print(res_str)
