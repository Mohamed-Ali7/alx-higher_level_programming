#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argsLen = len(sys.argv)
    result = 0

    for i in range(1, argsLen):
        result += int(sys.argv[i])
    print("{}".format(result))
