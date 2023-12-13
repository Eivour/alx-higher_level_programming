#!/usr/bin/python3

def uppercase(s):
    result = ''
    for char in s:
        result += '{}'.format(chr(ord(char) - 32))
    
    print(result)

# Example usage:
uppercase("hello")
