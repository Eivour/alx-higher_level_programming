#!/usr/bin/python3
for lowercase_ascii in range(ord('a'), ord('z') + 1):
    alphabet = chr(lowercase_ascii)

    if alphabet != 'q' and alphabet != 'e':
        print("{}".format(alphabet), end="")
