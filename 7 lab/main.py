from func_package import prepare_text


iterations = 5
text = 'Разворачивайтесь в марше! Словесной не место кляузе. Тише, ораторы! Ваше слово, товарищ маузер. Довольно жить законом, данным Адамом и Евой. Клячу истории загоним. Левой! Левой! Левой!'
modified_text = prepare_text(text)

for k in range(1, iterations+1):
    k_grams_list = [''.join(text[i-k:i]) for i in range(k, len(text)+k,k)]