# Author: Justin Mullins
# Course: SDEV300
# Date: 14Jun2020
# Lab4

# import modules
import sys
import numpy as np


def ask_to_play(function):
    # initialize variable
    user_input = ""

    if function == "start":
        # intro text for user
        print("Welcome to the Python Matrix Application")
        # get user input assign to variable user_input
        user_input = input("\nDo you want to play the Matrix Game? (Y/N): ")
    elif function == "replay":
        # get user input assign to variable user_input
        user_input = input("\nWould you like to play again? (Y/N): ")

    # returns true if y or Y
    if user_input.upper() == 'Y':
        np_matrix = enter_matrix()
        display_menu(np_matrix)
    # returns false is n or N
    elif user_input.upper() == 'N':
        print("\nThanks for playing the Python Matrix. Goodbye!")
    # incorrect input, exits
    else:
        print("\nIncorrect/unknown entry. Exiting..")
        sys.exit()


def create_matrix():
    # declare/initialize variables
    count = 1
    matrix = []

    # while statement to loop for 3 rows of matrix
    while count < 4:
        print("Please enter values for row {}".format(count))
        # try/except statement to catch value errors
        try:
            value_one = float(input("\tEnter first value:"))
            value_two = float(input("\tEnter second value:"))
            value_three = float(input("\tEnter third value:"))
            # creates list 'row' from input values
            row = [value_one, value_two, value_three]
            # appends row to list matrix
            matrix.append(row)
            # increment loop
            count += 1
        except ValueError:
            print("Please enter an integer or float value only.")
    # returns generated matrix
    return matrix


def enter_matrix():
    print("Please enter your first 3x3 matrix:")
    # runs create_matrix and assigns it to first_matrix
    first_matrix = create_matrix()
    # prints first matrix to screen
    print("\nYour first matrix\n")
    for row in first_matrix:
        print(row)

    print("\n\nPlease enter your second 3x3 matrix:")
    # runs create_matrix and assigns it to second_matrix
    second_matrix = create_matrix()
    # prints second matrix to screen
    print("\nYour second matrix\n")
    for row in second_matrix:
        print(row)

    np_matrix = np.array([first_matrix, second_matrix])
    return np_matrix


def display_menu(np_matrix):
    # displays user menu
    print("\nMATRIX OPERATION MENU"
          "\n\ta) Matrix Addition",
          "\n\tb) Matrix Subtraction",
          "\n\tc) Matrix Multiplication",
          "\n\td) Element by element multiplication")
    # get user input and assign to variable
    menu_select = input("Please select a matrix operation from the list above (a,b,c,d):")

    # runs function based off user input
    if menu_select == 'a':
        add_matrix(np_matrix)
        ask_to_play("replay")
    elif menu_select == 'b':
        subtract_matrix(np_matrix)
        ask_to_play("replay")
    elif menu_select == 'c':
        multiply_matrix(np_matrix)
        ask_to_play("replay")
    elif menu_select == 'd':
        element_multiply_matrix(np_matrix)
        ask_to_play("replay")
    else:
        print("Incorrect selection. Please try again.")
        display_menu(np_matrix)


def add_matrix(np_matrix):
    # adds elements in matrices
    added_matrix = np.add(np_matrix[0], np_matrix[1])
    # print output
    print("\nAdded Matrix\n")
    for row in added_matrix:
        print(row)

    # runs transpose and mean functions
    transpose_matrix(added_matrix)
    get_mean(added_matrix)


def subtract_matrix(np_matrix):
    # subtracts elements in matrices
    subtracted_matrix = np.subtract(np_matrix[0], np_matrix[1])
    # print output
    print("\nSubtracted Matrix\n")
    for row in subtracted_matrix:
        print(row)
    # runs transpose and mean functions
    transpose_matrix(subtracted_matrix)
    get_mean(subtracted_matrix)


def multiply_matrix(np_matrix):
    # multiplies matrices
    multiplied_matrix = np.matmul(np_matrix[0], np_matrix[1])
    # print output
    print("\nMultiplied Matrix\n")
    for row in multiplied_matrix:
        print(row)
    # runs transpose and mean functions
    transpose_matrix(multiplied_matrix)
    get_mean(multiplied_matrix)


def element_multiply_matrix(np_matrix):
    # multiplies elements in matrices
    ele_matrix = np.multiply(np_matrix[0], np_matrix[1])
    # print output
    print("\nElement by Element Multiplication Matrix\n")
    for row in ele_matrix:
        print(row)
    # runs transpose and mean functions
    transpose_matrix(ele_matrix)
    get_mean(ele_matrix)


def transpose_matrix(matrix):
    # transpose matrix
    transposed_matrix = matrix.T
    # print output
    print("\nTransposed Matrix\n")
    for row in transposed_matrix:
        print(row)


def get_mean(matrix):
    # get row and column means
    row_mean = matrix.mean(axis=1)
    column_mean = matrix.mean(axis=0)
    # print means for rows and columns
    print("\nRow Mean:", row_mean)
    print("\nColumn Mean:", column_mean)


def start():
    ask_to_play("start")


# runs main function
if __name__ == '__main__':
    start()
