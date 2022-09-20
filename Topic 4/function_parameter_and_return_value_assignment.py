"""
Program: function_parameter_and_return_value_assignment.py
Author: Alex Heinrichs
Last date modified: 09/20/2022

Defines a functin called multiply_string() that takes
a string message and a number n and
returns the string with message printed n times
"""


def multiply_string(string, n):
    """multiplies a string by n and returns the string
    :param string: this is the string to be multiplied
    :param n: number of times the string is multiplied
    :returns a string of string multiplied by n
    """

    # temp_string is defined to append to string variable
    temp_string = string

    # this loop iterates n - 1 amount of times (since string
    # already contains one iteration worth of string
    for i in range(0, n - 1):
        string += temp_string  # appends one instance of string each iteration
    # modified string variable is returned
    return string

if __name__ == '__main__':
    print(multiply_string('Python!', 4))
