# Function that asks user for input and displays min_max values
def main():
    print("*****************************************************")

    # Welcome text for application
    print("Welcome to the Minimum and Maximum Number Finder!" +
          "\nPlease enter five numbers to find the min and max of that set of numbers.\n")

    # Defines two lists: 'number_list' for user inputs and 'index_list' for the next number entered
    number_list = []
    index_list = ["first", "second", "third", "fourth", "fifth"]

    # try/except statement to only get integers from user input; otherwise exit
    try:
        # For loop to get user input and append to empty list 'number_list'
        for x in range(5):
            # Converts string input to int value
            input_value = int(input("Enter your {} number:".format(index_list[x])))
            number_list.append(input_value)

        # Get max and min numbers from 'number_list' elements and assign to variables
        min_value = min(number_list[0], number_list[1], number_list[2], number_list[3], number_list[4])
        max_value = max(number_list[0], number_list[1], number_list[2], number_list[3], number_list[4])

        # print statement that re-states inputted numbers and outputs results
        print("The maximum value of your five numbers ({}, {}, {}, {}, {}) are:\n"
              "Maximum = {}\n"
              "Minimum = {}\n\n".format(number_list[0], number_list[1], number_list[2], number_list[3],
                                        number_list[4], max_value, min_value))

        # Closing print statement that thanks user before exiting
        print("Thanks for using the Minimum and Maximum Number Finder! Goodbye!")
        print("*****************************************************")

    # except statement that catches an error when converting from string to int in above code
    except ValueError:
        print("Please only enter an integer. Restart and try again.")
        print("*****************************************************")


# Runs main() function
if __name__ == '__main__':
    main()
