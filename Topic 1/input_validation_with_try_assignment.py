"""
Program: input_validation_with_try_assignment.py
Author: Alex Heinrichs
Last date modified: 09/19/2022

Copied code from score averaging project and now
will be adding input validation
"""
# Some pseudocode copied from Mr. Peppers

# store a constant of the number of scores we will input: 3
NUM_SCORES = 3

# Prompt user for inputs
# store input as last_name
last_name = input("Enter your last name: ")
# added in this try except that will test to make sure the input is alphabet letters
try:
    # if else statement that will raise ValueError is last_name isn't alphabet letters
    if last_name.isalpha():
        print("Last name " + last_name + " accepted")
    else:
        raise ValueError("Bad input")
except:
    # If ValueError is raised then the variable will
    # enter this while loop at least once for a new input
    # (due to it not being alphabet letters)
    while not last_name.isalpha():
        last_name = input("Input not accepted, please enter only letters: ")
    print("Last name " + last_name + " accepted")

# store input as first_name
first_name = input("Enter your first name: ")
# added in same try except function as above
try:
    # if else statement that will raise ValueError is first_name isn't alphabet letters
    if first_name.isalpha():
        print("First name " + first_name + " accepted")
    else:
        raise ValueError("Bad input")
except:
    # If ValueError is raised then the variable will enter this while loop
    # at least once for a new input
    # (due to it not being alphabet letters)
    while not first_name.isalpha():
        first_name = input("Input not accepted, please enter only letters: ")
    print("First name " + first_name + " accepted")

# store input as age
age = input("Enter your age (from 0-125): ")
# added in same try except function as above except using isdigit and age parameters
try:
    # if else statement that will raise ValueError if age isn't a number from 0 to 125
    if age.isdigit() and 0 <= int(age) <= 125:
        print("Age " + age + " accepted")
    else:
        raise ValueError("Bad input")
except:
    while not age.isdigit() or int(age) < 0 or int(age) > 125:
        age = input("Input not accepted, please enter only positive numbers up to 125: ")
    print("Age " + age + " accepted")

# create a list to hold the scores
scores = []
# prompt user for the scores (do it constant times, use a new variable each time)
for x in range(NUM_SCORES):
    temp_score = input(f"Please enter score {str(x + 1)} (0-100): ")
    # added in this try except statement that will only allow digits from 0 to 100 to be
    # appended to the scores list
    try:
        if 0 <= int(temp_score) <= 100:
            print(temp_score + f" accepted for score {str(x + 1)}")
            scores.append(int(temp_score))
        else:
            raise ValueError("Bad Input")
    except:
        # If ValueError is raised then the variable will
        # enter this while loop at least once for a new input
        # (due to it not being a digit from 0 to 100)
        while not temp_score.isdigit() or int(temp_score) < 0 or int(temp_score) > 100:
            temp_score = input("Input not accepted. Please enter score between 0 and 100: ")
        print(temp_score + f" accepted for score {str(x + 1)}")
        scores.append(int(temp_score))

# calculate an average (sum each value and divide by the number of values)
# add all values in average variable
average = 0
for x in range(NUM_SCORES):
    average += scores.pop()
# now divide by NUM_SCORES
average = average / NUM_SCORES

# print output; should look like
# Rodriguez, Linda age: 21 average grade: 92.50

print(last_name + ", " + first_name + " age: " + age
      + " average grade: " + str(round(average, 2)))
