#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            print("{}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{}".format(str[i]), end="")
    print()
