# | 1 | 2 | 3 | 4 | 5 | 6 |
# | 2 | 3 | 1 | 6 | 4 | 5 |
from encrypt import encrypt
from decrypt import decrypt

file_path = r""
encryption_key = [
    [1, 2, 3, 4, 5, 6],
    [2, 3, 1, 6, 4, 5]
]
decryption_key = [
    [1, 2, 3, 4, 5, 6],
    [3, 1, 2, 5, 6, 4]
]


#encrypt(file_path, encryption_key)
decrypt(file_path, decryption_key)