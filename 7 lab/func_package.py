import re
import string



def prepare_text(text):
    pattern = re.compile("[а-я]+")
    text = text.translate(str.maketrans("", "", string.punctuation)).lower() # Удаление знаков препинания и перевод в нижний регистр
    text = ''.join([letter for letter in filter(pattern.match, text)]) # Убираем символы других алфавитов, кроме русского
    return text




    