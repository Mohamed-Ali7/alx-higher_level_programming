#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            upperChar = chr(ord(c) - 32)
        else:
            upperChar = c
        print("{}".format(upperChar), end="")
    print()
