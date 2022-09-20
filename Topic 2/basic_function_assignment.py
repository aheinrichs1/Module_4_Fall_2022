"""
Program: basic_function_assignment.py
Author: Alex Heinrichs
Last date modified: 09/20/2022

This code defines a function called hourly_employee_input
which asks  the user for a name (string), hours worked (int) and
an hourly pay rate (float)
and prints a string including the information
"""

# Defining function hourly_employee_input
def hourly_employee_input():
    """Asks user for name, hours worked, and pay rate and prints a string"""
    name = input("Please enter your name: ") # user input string
    try:
        hours_worked = int(input("Please enter your hours worked: "))
        # will throw error if not an int
        if hours_worked < 0: # throw error if negative value
            raise ValueError
        pay_rate = float(input("Please enter your pay rate: "))
        # will throw error if not a float
        if pay_rate < 0: # throws error if negative value
            raise ValueError
    except ValueError:
        raise ValueError
        # This will push an error to main so that
        # we can provide a custom message
    else:
        # if no error occurred, message will print
        print("Name: " + name + "\nHours worked: " + str(hours_worked)
              + "\nPay rate: " + str(pay_rate))

# driver code
if __name__ == "__main__":
    try: # checking for ValueError
        hourly_employee_input() # function call
    except ValueError:
        # custom error message
        print("ValueError occurred, please try again!")
