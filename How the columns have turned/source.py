import os


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
    derived_key = deriveKey(key)

    width = len(key)

    blocks = [pt[i:i + width] for i in range(0, len(pt), width)]
    blocks = transpose(blocks)

    ct = [blocks[derived_key.index(i + 1)][::-1] for i in range(width)]
    ct = flatten(ct)
    return ct


class PRNG:
    def __init__(self, seed):
        self.p = 0x2ea250216d705 # p = constant
        self.a = self.p # a = p
        self.b = int.from_bytes(os.urandom(16), 'big') # b = random number
        self.rn = seed # rn = seed

    def next(self):
        self.rn = ((self.a * self.rn) + self.b) % self.p
        return self.rn


def main():
    seed = int.from_bytes(os.urandom(16), 'big') # Random Seed
    rng = PRNG(seed) # PRNG gets called

    cts = ""

    for message in SUPER_SECRET_MESSAGES:
        key = str(rng.next()) # key is stringified from random number PRNG return rn
        ct = twistedColumnarEncrypt(message, key)
        cts += ct + "\n" # summation of ct in new lines

    with open('encrypted_messages.txt', 'w') as f:
        f.write(cts) # cts get written inside file

    dialog = "Miyuki says:\n"
    dialog += "Klaus it's your time to sign!\n"
    dialog += "All we have is the last key of this wierd encryption scheme.\n"
    dialog += "Please do your magic, we need to gather more information if we want to defeat Draeger.\n"
    dialog += f"The key is: {str(key)}\n"

    with open('dialog.txt', 'w') as f:
        f.write(dialog)


if __name__ == '__main__':
    main()
