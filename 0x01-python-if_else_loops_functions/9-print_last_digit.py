#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number)
    last_digit = number % 10
    return last_digit

if __name__ == "__main__":
    print(print_last_digit(98))
    print(print_last_digit(0))
    r = print_last_digit(-1024)
    print(r)
