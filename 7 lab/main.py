from func_package import prepare_text, count_entropy, build_graph


iterations = 5
H_outputs = []
text = 'Разворачивайтесь в марше! Словесной не место кляузе. Тише, ораторы! Ваше слово, товарищ маузер. Довольно жить законом, данным Адамом и Евой. Клячу истории загоним. Левой! Левой! Левой!'
modified_text = prepare_text(text)

for k in range(1, iterations+1):
    k_grams_list = [''.join(modified_text[i-k:i]) for i in range(k, len(modified_text)+k,k)]
    H_outputs.append(count_entropy(k_grams_list)/k)
    print(f'k = {k}: E = {H_outputs[k-1]/k}')

build_graph(iterations, H_outputs)