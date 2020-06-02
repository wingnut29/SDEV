# Author: Justin Mullins
# Course: SDEV300
# Date: 31May2020

# import random module
import random


# main function for lottery program
def main():
    # Defines variables
    lottery_loop = True

    # Prints welcome text
    print("*************************************")
    print("Welcome to the Python Lottery!"
          "\nChoose between either the Pick-3 or Pick-4 lottery.")

    # while loop to continue until user exits
    while lottery_loop is True:

        # Prints out menu text for user
        print("\nPlease choose from the following options:")
        print("1. Pick 3"
              "\n2. Pick 4"
              "\n3. Exit")

        # gets input from user and assigns to variable 'user_input'
        user_input = input("Please choose 1, 2 or 3 to select your option.")

        # if/elif/else statements to run code based on user input
        if user_input == "1":
            print("\nYou choose the Pick-3 Lottery.")
            # Gets three number value for pick-3 and assigns to variable 'number_value'
            number_value = pick_three()
            print("The Pick-3 number generated was: {}".format(number_value))
        elif user_input == "2":
            print("\nYou choose the Pick-4 Lottery.")
            # Gets four number value for pick-4 and assigns to variable 'number_value'
            number_value = pick_four()
            print("The Pick-4 number generated was: {}".format(number_value))
        elif user_input == "3":
            # sets variable 'lottery_loop' to False to exit while loop
            lottery_loop = False
        else:
            # Prints text in-case user enters incorrect selection
            print("\nIncorrect selection. Please try again.")

    # Runs once loop is exited if variable 'lottery_loop' is False
    if lottery_loop is False:
        exit_lottery()


# function that runs pick-three lottery number generator
def pick_three():
    # declare variables
    number_list = []
    number_string = ""
    count = 0

    # while loop to get random number and append it to list
    while count < 3:
        number_list.append(str(random.randrange(0, 10)))
        count += 1

    # Concatenate numbers in list to a single string
    number_string = "".join(number_list)

    # Returns string value
    return number_string


# function that runs pick-four lottery number generator
def pick_four():
    # declare variables
    number_list = []
    number_string = ""
    count = 0

    # while loop to get random number and append it to list
    while count < 4:
        number_list.append(str(random.randrange(0, 10)))
        count += 1

    # Concatenate numbers in list to a single string
    number_string = "".join(number_list)

    # Returns string value
    return number_string


# function to exit program
def exit_lottery():
    # exit text for program
    print("\nThank you for playing the Python Lottery!")
    print("*************************************")


# run mains function
if __name__ == '__main__':
    main()
