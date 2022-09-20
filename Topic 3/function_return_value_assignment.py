"""
Program: basic_function_assignment.py
Author: Alex Heinrichs
Last date modified: 09/20/2022

This code defines a function called hourly_employee_input
which asks  the user for a name (string), hours worked (int) and
an hourly pay rate (float)
and returns information as a string

This assignment now defines another function called
weekly_pay, which will take in values hours_worked and
pay_rate and returns the calculated weekly pay
"""


# Defining function hourly_employee_input
def hourly_employee_input():
    """Asks user for name, hours worked, and pay rate
    :returns string of information
    :raises ValueError if inputs are negative or not numbers
     """
    name = input("Please enter your name: ")  # user input string
    try:
        hours_worked = int(input("Please enter your hours worked: "))
        # will throw error if not an int
        if hours_worked < 0:  # throw error if negative value
            raise ValueError
        pay_rate = float(input("Please enter your pay rate: "))
        # will throw error if not a float
        if pay_rate < 0:  # throws error if negative value
            raise ValueError
    except ValueError:
        raise ValueError
        # This will push an error to main so that
        # we can provide a custom message
    else:
        # if no error occurred: returns a string of name variable
        # and weekly pay
        return ("Name: " + name + "\nWeekly pay: "
                + str(weekly_pay(hours_worked, pay_rate)))  # function call


def weekly_pay(hours_worked, pay_rate):
    """Calculates weekly pay by multiplying hours_worked by pay_rate
    :param hours_worked represents hours worked in the week
    :param pay_rate represents pay rate per hour worked
    :returns float variable of hours_worked multiplied by pay_rate
    """
    return hours_worked * pay_rate


# driver code
if __name__ == "__main__":
    try:  # checking for ValueError
        print(hourly_employee_input())  # function call
    except ValueError:
        # custom error message
        print("ValueError occurred, please try again!")
