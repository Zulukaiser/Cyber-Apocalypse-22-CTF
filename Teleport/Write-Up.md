# Cyber Apocalypse 2022 CTF - Rev: Teleport

In this challenge we are given an executable file named "*teleport*".
When we try to run it, we are given the text "Missing password", so when we want to run the program, we have to provide it with a password.
We should have a look at the program in Ghidra, to better understand how it is working.
After we opened the executable in Ghidra and let Ghidra analyze it, we can navigate to the functions folder.
We see a lot of *FUN_00100???* functions. When we go through those functions we don't get any information other than some DAT-Blocks being compared to certain characters.
These characters contain the characters **H, T, B, {, }, p, g, 0, 1, h, t** and so on. I guess those are the characters, that our flag is made of.
Let's click on on a DAT-block to see where it's stored, or what the code does with it.
In the code browser we can see the DAT-blocks, but they aren't filled yet. We also can see that each DAT-block has a cross reference to a *FUN_00100???* function. If we are lucky these DAT-blöocks are in order with the contents of the flag.
Let's test that theory. We know that the flag has following format:
**HTB{SOMETHING}**
If we take the first DAT-block, named "*DAT_0030280*" and click on the XREF function *FUN_00100f6a* we see that this DAT-block checks for the letter **H**.
Okay, we can do the same procedure from the top to bottom of the DAT-blocks.
We get following mapping:

+ DAT_00303280: H
+ DAT_00303281: T
+ DAT_00303282: B
+ DAT_00303283: {
+ DAT_00303284: h
+ DAT_00303285: 0
+ DAT_00303286: p
+ DAT_00303287: p
+ DAT_00303288: 1
+ DAT_00303289: n
+ DAT_0030328a: g
+ DAT_0030328b: _
+ DAT_0030328c: t
+ DAT_0030328d: h
+ DAT_0030328e: r
+ DAT_0030328f: u
+ DAT_00303290: _
+ DAT_00303291: t
+ DAT_00303292: h
+ DAT_00303293: 3
+ DAT_00303294: _
+ DAT_00303295: s
+ DAT_00303296: p
+ DAT_00303297: 4
+ DAT_00303298: c
+ DAT_00303299: 3
+ DAT_0030329a: _
+ DAT_0030329b: t
+ DAT_0030329c: 1
+ DAT_0030329d: m
+ DAT_0030329e: 3
+ DAT_0030329f: _
+ DAT_003032a0: c
+ DAT_003032a1: 0
+ DAT_003032a2: n
+ DAT_003032a3: t
+ DAT_003032a4: 1
+ DAT_003032a5: n
+ DAT_003032a6: u
+ DAT_003032a7: u
+ DAT_003032a8: m
+ DAT_003032a9: !
+ DAT_003032aa: }

Flag: HTB{h0pp1ng_thru_th3_sp4c3_t1m3_c0nt1nuum!}

We have our flag!!!
