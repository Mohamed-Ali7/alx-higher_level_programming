#!/usr/bin/python3

"""module contains a script reads stdin line by line and computes metrics"""


import sys


total_size = 0
status = {"200": 1, "301": 1, "400": 1, "401": 1,
          "403": 1, "404": 1, "405": 1, "500": 1}
printable_status = {}
try:
    while True:
        for r in range(10):
            line = sys.stdin.readline()
            words = line.split()
            status_code = words[-2]
            total_size += int(words[-1])
            if status_code in status:
                printable_status[status_code] = status[status_code]
                status[status_code] += 1

        print(f"File size: {total_size}")
        for key in sorted(printable_status):
            print(f"{key}: {printable_status[key]}")
except KeyboardInterrupt as ex:
    print(f"File size: {total_size}")
    for key in sorted(printable_status):
        print(f"{key}: {printable_status[key]}")
