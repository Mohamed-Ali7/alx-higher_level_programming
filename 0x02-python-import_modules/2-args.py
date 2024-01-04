#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argsLen = len(sys.argv) - 1

    if argsLen == 1:
        argString = "argument:"
    elif argsLen == 0:
        argString = "arguments."
    else:
        argString = "arguments:"

    print("{} {}".format(argsLen, argString))

    for i in range(1, argsLen + 1):
        print("{}: {}".format(i, sys.argv[i]))
