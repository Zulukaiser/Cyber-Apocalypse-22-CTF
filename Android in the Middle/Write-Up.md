# Cyber Apocalypse 2022 HTB CTF - Crypto: Android in the middle
---------------------------------------------------------------

In this challenge we were given a python script called "*source.py*" and a Docker instance.
Let's connect with the Docker instance.

```console
connect $IP $PORT
```

When we connect with the instance some text is displayed and we are prompted to "*Enter The Public Key of The Memory:*".
Obviously we don't know the public key of the memory. But we can check the "*source.py*" file.
When we look at the python script, we can see some server stuff happening, which we can ignore. We should take a closer look to the *main()* function.
We can see the text that is printed on the terminal if we access the docker instance. Aslo we see a variable *c* and a variable *C* as well as a input variable *M* which are equal to:

```python
c = random.randrange(2, p - 1)
C = pow(g, c, p)
M = recieveMessage(s, "Enter The Public Key of The Memory: ")
```

We know that p is a huge number, so we can't predict what *c* or *C* are. But we can set the value of *M* with our user input.

Further down in the *main()* function, a new variable calles *shared_secret* is introduced.

```python
shared_secret = pow(M, c, p)
```

As we know *c* is an unpredictabel, huge number and *p* also, but we can have an influence on *M* let's figure out how we can know the shared_secret.

If *M* is equal to *0*, *shared_secret* is also *0*, because 0 to the power of anything is still 0.
Now we can further analyze the *main()* function. A new variable called *encrypted_sequence* is introduced.
We can fill in the value of this variable with another user input. a function called *decrypt()* decrypts the message and stores the return value in *sequence*.
An if-statement is checking if *sequence == b'Initialization Sequence - 0'*. If the statement is true we get our flag.
So now we know following things:
+ **c**, **C** are random numbers that are probably huge
+ we can input the value for **M**
+ if **M = 0** than the **shared_secret = 0**
+ we can input the value for **encrypted_sequence**
+ decrypted sequence must be equal to **b'Initialization Sequence - Code 0'**

Ok, let's get a script together that can encrypt our sequence, so we know our input that we have to give.
I just copied the *source.py* file and replaced the server stuff with some local syntax.
We now should make our *encrypt()* function. We need to provide the *shared_secret* and the *encrypted_sequence* variable.
Now we calculate the **key** and **cipher** exactly the same as *source.py* does in the *decrypt()* function.
After that we encrypt our message:

```python
encrypted_message = cipher.encrypt(plain.encode(encoding = 'UTF-8'))
```
Perfect! Now we have to call our *encrypt()* function in the *main()* function and provide it with the *shared_secret* which should be equal to 0 and the plain text,
which is our *sequence*. Run the script and you should get your hex string which you can provide as the second input.
If we connect to the docker instance again, we give 0 as **M** and our hex string as **encrypted_sequence**.

You get the flag!
