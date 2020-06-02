# Author: Justin Mullins
# Course: SDEV300
# Date: 31May2020

# import modules
from numpy import arange
from math import pi, sin, cos, sqrt, log10


# main function for math program
def main():
    print("Below are the results (in coord form) for sin(x) from -2pi to 2pi with an increment of pi/64:")
    # Runs function 'math_sin()'
    math_sin()
    print("\n\n")

    print("Below are the results (in coord form) for cos(x) from -2pi to 2pi with an increment of pi/64:")
    # Runs function 'math_cos()'
    math_cos()
    print("\n\n")

    print("Below are the results (in coord form) for sqrt(x) from 0 to 200 with an increment of .5:")
    # Runs function 'math_sqrt()'
    math_sqrt()
    print("\n\n")

    print("Below are the results (in coord form) for log10(x) from 0 to 200 with an increment of .5:")
    # Runs function 'math_log()'
    math_log()
    print("\n\n")


def math_sin():
    # Define/declare variables
    start_value = (-2 * pi)
    end_value = (2 * pi)
    increment = (pi / 64)

    # for statement using numpy's arrange function for float values
    for x in arange(start_value, end_value, increment):
        # using the math sin function and assign it to variable 'result'
        result = sin(x)
        # print output
        print("({}, {})".format(x, result))


def math_cos():
    # Define/declare variables
    start_value = (-2 * pi)
    end_value = (2 * pi)
    increment = (pi / 64)

    # for statement using numpy's arrange function for float values
    for x in arange(start_value, end_value, increment):
        # using the math cos function and assign it to variable 'result'
        result = cos(x)
        # print output
        print("({}, {})".format(x, result))


def math_sqrt():
    # Define/declare variables
    start_value = 0
    end_value = 200
    increment = .5

    # for statement using numpy's arrange function for float values
    for x in arange(start_value, end_value, increment):
        # using the math sqrt function and assign it to variable 'result'
        result = sqrt(x)
        # print output
        print("({}, {})".format(x, result))


def math_log():
    # Define/declare variables
    start_value = 0
    end_value = 200
    increment = .5

    # for statement using numpy's arrange function for float values
    for x in arange(start_value, end_value, increment):
        # try/except statement to catch domain error
        try:
            # using the math log function and assign it to variable 'result'
            result = log10(x)
            # print output
            print("({}, {})".format(x, result))
        except ValueError as e:
            print(str(e))


# run mains function
if __name__ == '__main__':
    main()
