#!/usr/bin/python3


def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter using ASCII values
        if ord('a') <= ord(char) <= ord('z'):
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end="")
        else:
            # Print the character as it is if it's not a lowercase letter
            print("{}".format(char), end="")
    print()  # Add a new line after printing the modified string


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
