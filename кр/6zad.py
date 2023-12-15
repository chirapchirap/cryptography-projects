import numpy as np

encoding = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
        'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
key = np.array([[1, 1, 0], [0, 1, 1], [1, 1, 0]])
flag = False
try: 
    inverse_key = [list(map(int, arr)) for arr in np.linalg.inv(key)]
except np.linalg.LinAlgError as error_msg:
    flag = True
    print(f'Не может быть ключа дешифрования(обратной матрицы к ключу): Ошибка -> {error_msg}')
    print('-'*10)
    
txt = 'корова'

def Foo(t, k):
    msg_codes = [encoding.index(let) for let in t]
    wrapped_msg_codes = list(msg_codes[i:i + len(k)] for i in range(0, len(msg_codes), len(k)))
    conv_codes = [code % len(encoding) for code in np.concatenate([np.dot(vector, k) for vector in wrapped_msg_codes])]
    conv_txt = [encoding[code] for code in conv_codes]
    return conv_txt


enc_txt = Foo(txt, key)
print('Зашифрованный текст:', enc_txt)
print('-'*10)

if flag == False:
    dec_txt = Foo(enc_txt, inverse_key)
    print('Расшифрованный текст:', dec_txt)
    print('-'*10)