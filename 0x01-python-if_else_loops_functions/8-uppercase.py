#!/usr/bin/python3


def uppercase(s):
    result = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(uppercase_char)
        else:
            result += "{}".format(char)

    print(result)


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
