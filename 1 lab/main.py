# 9 вариант m=256, k=(a, b) = (21,57).
from encrypt import encrypt
from decrypt import decrypt
file_path = r"C:\Users\User\OneDrive\Рабочий стол\1.pdf"

encrypt(file_path, a=21, b=57, mod=256)
decrypt(file_path, a=21, b=57, mod=256)
