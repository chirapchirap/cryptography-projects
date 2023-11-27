round_quantity = 3
key = 255
shift1 = 2
shift2 = 5


def use_feistel_cipher_for_encryption(num):
    bits = bin(num)[2:].zfill(8)
    left_block = bits[:len(bits)//2]
    right_block = bits[len(bits)//2:]
    a = 0
    while a < round_quantity:
        left_block, right_block = right_block[-4:], bin(int(left_block, 2) ^ ((int(right_block, 2)<<shift1) ^ (int(right_block, 2)<<shift2) ^ key))[2:].zfill(4)[-4:]
        a+=1
    return int(left_block+right_block, 2)


def use_feistel_cipher_for_decryption(num):
    bits = bin(num)[2:].zfill(8)
    left_block = bits[:len(bits)//2]
    right_block = bits[len(bits)//2:]
    a = 0
    while a < round_quantity:
        left_block, right_block = bin(int(right_block, 2) ^ ((int(left_block, 2)<<shift1) ^ (int(left_block, 2)<<shift2) ^ key))[2:].zfill(4)[-4:], left_block[-4:]
        a+=1
    return int(left_block+right_block, 2)