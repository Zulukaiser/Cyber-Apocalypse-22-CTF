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
Then we can calculate our **width**, which is 15 and can then slice our encrypted_message into an array.

Now we can make a new array and feed it with the blocks in order of the derived_key.
We then can switch the new blocks around to fit them together. I just tried the values out, by making a known plain text,
encrypting it and feeding it to the decrypt function.
After that we have to take the first characters in every block and put them in the first block, then take the second characters of each block and put them in the second block and so on and on.
The second to last step is to reverse the strings in each block again.
Last but not least we can flatten the array and print it out.
```python
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
```
If we did everything correct, we get 4 lines of readable strings with length of 105 characters in the terminal.
We have to put spaces after the words and we can then search for the string "*HTB*".
The flag is in the format: **HTB{SOMETHING}**
Now the content in the brackets is everything after the *HTB* string in line 3.

We got it!!!
