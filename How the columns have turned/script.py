import os


key_int = 729513912306026

with open('super_secret_messages.txt', 'r') as f:
    SUPER_SECRET_MESSAGES = [msg.strip() for msg in f.readlines()] #super secret message gets read


def deriveKey(key):
    derived_key = [] # derived key is an array

    for i, char in enumerate(key): #key gets looped through 
        previous_letters = key[:i] # array where previous letters get written in counter place of key
        new_number = 1
        for j, previous_char in enumerate(previous_letters):
            if previous_char > char:
                derived_key[j] += 1
            else:
                new_number += 1
        derived_key.append(new_number)
    return derived_key


def transpose(array):
    return [row for row in map(list, zip(*array))]


def flatten(array):
    return "".join([i for sub in array for i in sub])


def twistedColumnarEncrypt(pt, key):
    derived_key = [13, 5, 14, 10, 3, 8, 15, 4, 6, 9, 1, 11, 2, 7, 12]

    width = len(key)

    blocks = [pt[i:i + width] for i in range(0, len(pt), width)]
    #print(f'Raw Blocks: {blocks}\n')
    blocks = transpose(blocks)
    #print(f'Transposed Blocks: {blocks}\n')

    ct = [blocks[derived_key.index(i + 1)][::-1] for i in range(width)]
    #print(f'Ct Array: {ct}\n')
    ct = flatten(ct)
    #print(f'Ct: {ct}\n')
    return ct

def twistedColumnarDecrypt(cipher, key):
    #print(cipher)
    ct_array = []
    derived_key = [13, 5, 14, 10, 3, 8, 15, 4, 6, 9, 1, 11, 2, 7, 12]
    width = len(key)
    ct_array = [cipher[i:i + 7] for i in range(0, len(cipher), 7)]
    new_ct_array = [ct_array[derived_key.index(i + 1)][::-1] for i in range(width)]
    offset = 1
    final_ct = [new_ct_array[2-offset], new_ct_array[3-offset], new_ct_array[7-offset], new_ct_array[9-offset], new_ct_array[14-offset], new_ct_array[4-offset], new_ct_array[12-offset], new_ct_array[10-offset], new_ct_array[8-offset], new_ct_array[6-offset], new_ct_array[13-offset], new_ct_array[1-offset], new_ct_array[5-offset], new_ct_array[15-offset], new_ct_array[11-offset]]
    decrypted = ""
    for j in range(7):    
        for i in range(width):
            string = final_ct[i]
            val = string[j]
            decrypted += val

    array_rev = ['', '', '', '', '', '', '']
    cnt = 0
    for i in range(0, 105, 15):
        string = ''
        for j in range(15):
            string += decrypted[i+j]
        array_rev[cnt]= string
        cnt = cnt + 1

    array_rev = array_rev[::-1]

    decrypted = ""
    for j in range(7):    
        string = array_rev[j]
        decrypted += string

    print(f'{decrypted}\n')


def main():
    cts = ""

#    for message in SUPER_SECRET_MESSAGES:
#        key = str(key_int) # key is stringified from random number PRNG return rn
#        ct = twistedColumnarEncrypt(message, key)
#        cts += ct + "\n" # summation of ct in new lines

#    with open('encrypted_messages.txt', 'w') as f:
#        f.write(cts)

    with open('encrypted_messages.txt', 'r') as g:
        encrypted = [msg.strip() for msg in g.readlines()]
    for message in encrypted:
        key = str(key_int) # key is stringified from random number PRNG return rn
        ct = twistedColumnarDecrypt(message, key)

if __name__ == '__main__':
    main()
