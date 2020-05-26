# import for sys
import sys


# Function that asks user for input and displays min_max values
def main():
    print("*****************************************************")

    # Welcome text for application
    print("Welcome to the Python Calculator!\n\n")

    # Menu selection
    print("What calculation do you want to perform?\n"
          "Enter 1,2,3,4 or 5 to choose your selection.\n")
    print("1) Addition (+)\n"
          "2) Subtraction (-)\n"
          "3) Division (/)\n"
          "4) Multiplication (*)\n"
          "5) Modulus (%)\n")

    # Get user input and assign to variable 'user_input'
    user_input = input("What is your selection?")

    # try/except statement in-case number is not int
    try:
        # if/elif/else statements to check user input value and do correct calculation
        if user_input == "1":
            print("You selected addition.")

            # Gets number inputs from user, converts to int and assigns to variables
            number_1 = int(input("Please enter your first number: "))
            number_2 = int(input("Please enter your second number: "))

            # Gets result of calculation and assigns to variable 'result'
            result = number_1 + number_2

            # prints results
            print("The result of {} + {} is {}.\n".format(number_1, number_2, result))
            print("Thank you for using the Python Calculator! Goodbye!")
        elif user_input == "2":
            print("You selected subtraction.")

            # Gets number inputs from user, converts to int and assigns to variables
            number_1 = int(input("Please enter your first number: "))
            number_2 = int(input("Please enter your second number: "))

            # Gets result of calculation and assigns to variable 'result'
            result = number_1 - number_2

            # prints results
            print("The result of {} - {} is {}.\n".format(number_1, number_2, result))
            print("Thank you for using the Python Calculator! Goodbye!")
        elif user_input == "3":
            print("You selected division.")

            # Gets number inputs from user, converts to int and assigns to variables
            number_1 = int(input("Please enter your first number: "))
            number_2 = int(input("Please enter your second number: "))

            # if statement for is second number input is 0
            if number_2 == 0:
                print("You cannot divide by zero. Please restart and try again.")
                # exits application
                sys.exit()
            else:
                # Gets result of calculation and assigns to variable 'result'
                result = number_1 / number_2

                # prints results
                print("The result of {} / {} is {}.\n".format(number_1, number_2, result))
                print("Thank you for using the Python Calculator! Goodbye!")
        elif user_input == "4":
            print("You selected multiplication.")

            # Gets number inputs from user, converts to int and assigns to variables
            number_1 = int(input("Please enter your first number: "))
            number_2 = int(input("Please enter your second number: "))

            # Gets result of calculation and assigns to variable 'result'
            result = number_1 * number_2

            # prints results
            print("The result of {} * {} is {}.\n".format(number_1, number_2, result))
            print("Thank you for using the Python Calculator! Goodbye!")
        elif user_input == "5":
            print("You selected modulus.")

            # Gets number inputs from user, converts to int and assigns to variables
            number_1 = int(input("Please enter your first number: "))
            number_2 = int(input("Please enter your second number: "))

            # if statement for is second number input is 0
            if number_2 == 0:
                print("You cannot divide by zero. Please restart and try again.")
                # exits application
                sys.exit()
            else:
                # Gets result of calculation and assigns to variable 'result'
                result = number_1 % number_2

                # prints results
                print("The result of {} % {} is {}.\n".format(number_1, number_2, result))
                print("Thank you for using the Python Calculator! Goodbye!")
        else:
            print("Incorrect selection. Please restart and try again.")
            # exits application
            sys.exit()
    except ValueError:
        print("Please only enter an integer. Restart and try again.")
        print("*****************************************************")


# Runs main() function
if __name__ == '__main__':
    main()
