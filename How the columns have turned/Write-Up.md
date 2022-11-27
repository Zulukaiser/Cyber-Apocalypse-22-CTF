# Cyber Apocalypse 2022 - Crypto: How the columns have turned
--------------------------------------------------------------

In the "How the columns have turned" challenge we were given some files:
+ dialog.txt
+ source.py
+ encrypted_messages.txt

If we open the dialog.txt file we can see a conversation and some key is given to us.
**key = 729513912306026**

We should remember the key, because it could prove importnant.
In the encrypted_messages.txt file we see a bunch of encrypted data. Note that all the lines are exactly 105 characters long.
Let's have a look at the source.py file, maybe we can get some clues about the encryption mechanism.
Now we can have a look at the *main()* function.
We see a random generated *seed* variable and a pseudo-random-generated-number variable called *rng*
In line 62 we iterate through our messages, generate a key with the *rng* variable and store the encrypted message in *ct*.
ct gets added to cts with a new line character at the end. The encrypted *cts* variable gets written to encrypted_messages.txt

We have no way to calculate the key, that is used to encrypt the messages, but we have a momentarily snapshot with our encrypted_messages.txt file
and with our key from the dialog.txt file. So we can try to reconstruct and decrypt our encrypted_messages.
Let's analyze how the encryption works:
```python
def twistedColumnarEncrypt(pt, key):
    derived_key = deriveKey(key)

    width = len(key)

    blocks = [pt[i:i + width] for i in range(0, len(pt), width)]
    blocks = transpose(blocks)

    ct = [blocks[derived_key.index(i + 1)][::-1] for i in range(width)]
    ct = flatten(ct)
    return ct
```

We see that some list operations are done. The encryption mechanism slices the message in blocks of the size **width** and transposes these blocks.
The values of each block are also reversed. In the end the list is flattened and returned as a string.
Now that we know how the encryption works, we can write our own script to decrypt our messages.

First we can calculate the **derived_key** by providing the function *deriveKey()* our key from the dialog.txt file.
Then we can calculate our **width**, which is 15. We need to create a **new_key**, because in Line 32 we take the sublist of blocks on the index where **derived_key** has the value i+1 from 1 to 15. So we need to reverse this indexing technique by doing the exact same as in Line 32, but we will do the same technique as in Line 32 again later in the code. We also need to calculate our new subarray length by dividing the length of the cipher by the **width**.We can then slice our encrypted_message into a list called **ct_array**, by doing Line 29, so to speak the exact same operation as in the encryption function. After that we need to order the sublists with our **new_key**. Second to last we transpose this list and flatten it. Voila we have our decryption working!

```python
def twistedColumnarDecrypt(cipher, key):
    derived_key = deriveKey(key)
    new_key = []
    width = len(key)
    length = int(len(cipher)/width)
    for i in range(width):
        a = derived_key.index(i + 1) + 1
        new_key.append(a)

    ct_array = [cipher[i:i + length] for i in range(0, len(cipher), length)]
    blocks = [ct_array[new_key.index(i + 1)][::-1] for i in range(width)]
    blocks = transpose(blocks)
    pt = flatten(blocks)
    return pt
```
If we did everything correct, we get an *output.txt* file where we have the decrypted lines.
We have to put spaces after the words and we can then search for the string "*HTB*".
The flag is in the format: **HTB{SOMETHING}**
Now the content in the brackets is everything after the *HTB* string in line 3.

We got it!!!
