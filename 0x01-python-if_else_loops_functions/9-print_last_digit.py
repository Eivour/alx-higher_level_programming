#!/usr/bin/python3


def print_last_digit(number):
    # Ensure the number is positive
    number = abs(number)

    # Get the last digit
    last_digit = number % 10

    # Print the last digit
    print(last_digit, end='')

    # Return the last digit
    return last_digit


# Test cases
print_last_digit(98)
print_last_digit(0)
result = print_last_digit(-1024)
print(result)
