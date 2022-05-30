# Cyber Apocalypse 2022 CTF - Rev: Omega One
---------------------------------------------

In this challenge we were given an executabel and a "*output.txt*" file.
In the text file we can find 33 names written. If we try to execute the program thats provided to us, it immediately exits.
Let's view the code in Ghidra.
We can navigate to the functions folder and look through the functions. There isn't much interesting in those functions except for function **_FUN_00100b4c_**, which has an awful lot of names in it.
We can have a look at the DAT-blocks that are in the same line as th names, maybe there is something interesting in them.
If we take *DAT_00102149* we see that this DAT-block corresponds to the character **"k"**.
Some names in the function **_FUN_00100b4c_** are behind a DAT-block and not in plain text.
Let's bring the *output.txt* file into our thoughts. We know that each name corresponds to a character. Maybe we can map those characters to the *output.txt* file.
We get the following results:

H Crerceon
T Ezains
B Ummuh
{ Zonnu
l Vinzo
1 Cuzads
n Emoi
3 Ohols
4 Groz'ens
r Ukox
_ Ehnu
t Pheilons
1 Cuzads
m Khehlan
3 Ohols
_ Ehnu
b Munis
u Inphas
t Pheilons
_ Ehnu
p Dut
r Ukox
3 Ohols
t Pheilons
t Pheilons
y Zimil
_ Ehnu
s Honzor
l Vinzo
0 Ukteils
w Falnain
! Dhohmu
} Baadix

This seems to be our flag already!

HTB{l1n34r_t1m3_but_pr3tty_sl0w!}