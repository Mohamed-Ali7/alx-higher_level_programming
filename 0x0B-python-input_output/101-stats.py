#!/usr/bin/python3

"""module contains a script reads stdin line by line and computes metrics"""


import sys


total_size = 0
i = 0
status = {"200": 1, "301": 1, "400": 1, "401": 1,
          "403": 1, "404": 1, "405": 1, "500": 1}
printable_status = {}
try:
    for line in sys.stdin:
        words = line.split()
        status_code = words[-2]
        total_size += int(words[-1])
        if status_code in status:
            printable_status[status_code] = status[status_code]
            status[status_code] += 1
        if i == 10:
            print(f"File size: {total_size}")
            i = 1
            for key in sorted(printable_status):
                print(f"{key}: {printable_status[key]}")
        else:
            i += 1
except KeyboardInterrupt as ex:
    print(f"File size: {total_size}")
    for key in sorted(printable_status):
        print(f"{key}: {printable_status[key]}")
