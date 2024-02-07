#!/usr/bin/python3

"""module contains a script reads stdin line by line and computes metrics"""


import sys


total_size = 0
i = 1
status = {"200": 1, "301": 1, "400": 1, "401": 1,
          "403": 1, "404": 1, "405": 1, "500": 1}
printable_status = {}

try:
    for line in sys.stdin:
        words = line.split()
        if len(words) >= 2:
            status_code = words[-2]
            total_size += int(words[-1])
            if status_code in status:
                printable_status[status_code] = status[status_code]
                status[status_code] += 1
        if i == 10:
            print("File size: {:d}".format(total_size))
            for key, value in sorted(printable_status.items()):
                print("{}: {:d}".format(key, value))
            i = 1
        else:
            i += 1

    print("File size: {:d}".format(total_size))
    for key, value in sorted(printable_status.items()):
        print("{}: {:d}".format(key, value))
except KeyboardInterrupt as ex:
    print("File size: {:d}".format(total_size))
    for key, value in sorted(printable_status.items()):
        print("{}: {:d}".format(key, value))
