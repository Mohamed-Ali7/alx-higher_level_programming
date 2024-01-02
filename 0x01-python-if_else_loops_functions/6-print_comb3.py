#!/usr/bin/python3
for i in range(0, 10):
    for n in range(i+1, 10):
        print('{}{}'.format(i, n), end='')
        if n != 9 or i != 8:
            print(', ', end='')
print()
