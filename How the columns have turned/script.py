key_int = 729513912306026

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

def twistedColumnarDecrypt(cipher, key):
    derived_key = deriveKey(key) # Get derived_key
    width = len(key)
    length = int(len(cipher)/width) # Get length of sublists, after transposing in the enryption function
    new_key = [derived_key.index(i + 1) + 1 for i in range(width)]  # Generate new_key

    ct_array = [cipher[i:i + length] for i in range(0, len(cipher), length)] # Slice the cipher in sublists with corresponding length
    blocks = [ct_array[new_key.index(i + 1)][::-1] for i in range(width)]   # Order the sublists according to the new_key
    blocks = transpose(blocks)
    pt = flatten(blocks)
    return pt

def main():
    cts = ""

    with open('encrypted_messages.txt', 'r') as g:
        encrypted = [msg.strip() for msg in g.readlines()]
    for message in encrypted:
        key = str(key_int) # key is stringified from random number PRNG return rn
        ct = twistedColumnarDecrypt(message, key)
        cts += ct +'\n'

        with open('output.txt', 'w') as f:
            f.write(cts)
        
if __name__ == '__main__':
    main()
