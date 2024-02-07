#!/usr/bin/python3

"""module contains a script reads stdin line by line and computes metrics"""


import sys


total_size = 0
i = 1
status = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        words = line.split()
        status_code = words[-2]
        total_size += int(words[-1])
        if status_code in status:
            status[status_code] += 1
        if i == 10:
            print("File size: {:d}".format(total_size))
            for key, value in sorted(status.items()):
                if value > 0:
                    print("{}: {:d}".format(key, value))
            i = 1
        else:
            i += 1

    print("File size: {:d}".format(total_size))
    for key, value in sorted(status.items()):
        if value > 0:
            print("{}: {:d}".format(key, value))
except KeyboardInterrupt as ex:
    print("File size: {:d}".format(total_size))
    for key, value in sorted(status.items()):
        if value > 0:
            print("{}: {:d}".format(key, value))
