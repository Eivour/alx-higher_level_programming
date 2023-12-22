#!/usr/bin/python3


def print_list_integer(my_list=[]):
    for integer in my_list:
        print("{:d}".format(integer))

#Example case
integers = [2, 4, 6, 8, 10]
print_list_integer(integers)