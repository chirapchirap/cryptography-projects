from re import compile 
from collections import Counter
from string import punctuation
from math import log2
import matplotlib.pyplot as plt



def prepare_text(text):
    pattern = compile("[а-я]+")
    text = text.translate(str.maketrans("", "", punctuation)).lower() # Удаление знаков препинания и перевод в нижний регистр
    text = ''.join([letter for letter in filter(pattern.match, text)]) # Убираем символы других алфавитов, кроме русского
    return text


def count_entropy(k_grams):     # Подсчет энтропии
    frequency = Counter(k_grams)
    H = sum([(value/len(k_grams)) * log2(value/len(k_grams)) for value in frequency.values()])
    return abs(H)


def build_graph(iters, H):
    x = [i for i in range(1, iters+1)]
    y = H
    plt.title("График зависимости Hk(T) от k")  # название графика
    plt.xlabel("k")  # ось абсцисс
    plt.ylabel("Hk(T)")  # ось ординат
    plt.grid()  # включение отображения сетки
    plt.scatter(x, y)  # для отображения точек на графике
    plt.plot(x, y)  # для отображения линии на графике
    plt.show()  # показать график