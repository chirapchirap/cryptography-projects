# | 1 | 2 | 3 | 4 | 5 | 6 |
# | 2 | 3 | 1 | 6 | 4 | 5 |
from encrypt import encrypt
from decrypt import decrypt
file_path = r""
key = [
    [1, 2, 3, 4, 5, 6],
    [2, 3, 1, 6, 4, 5]
]

encrypt(file_path, key)
decrypt(file_path, key)
