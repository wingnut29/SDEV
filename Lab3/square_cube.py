# Author: Justin Mullins
# Class: SDEV300
# Date: 8JUNE20


def display_menu():
    # creates display menu
    print("\n1.Display the Square and Cube for Integers ranging from 1 to 100",
          "\n2.Search the sets for a specific Integer and display the Square and Cube values",
          "\n3.Display the Union of Square and Cube sets",
          "\n4.Display the Intersection of Square and Cube sets",
          "\n5.Display the Difference of Square and Cube sets",
          "\n6.Exit the program")

    # get user input and assign to 'user_input'
    user_input = int(input("\nChoose a selection from the above menu (1-6):"))
    return user_input


def show_square_cube(number=None):
    # if user enters a number to square and cube runs
    if number is not None:
        # Calculate squared values
        squared_number = number * number
        # Calculate cubed values
        cubed_number = squared_number * number

        print(
            "\nInt: {}".format(number),
            "\nSquared: {}".format(squared_number),
            "\nCubed: {}".format(cubed_number)
        )
    else:
        for number in range(1, 101):
            # Calculate squared values
            squared_number = number * number
            # Calculate cubed values
            cubed_number = squared_number * number

            print(
                "\nInt: {}".format(number),
                "\nSquared: {}".format(squared_number),
                "\nCubed: {}".format(cubed_number)
            )


def get_squared_set():
    # declare variables
    squared_set = set()

    # for loop to square numbers in range 1-100
    for number in range(1, 101):
        # Calculate squared values
        squared_number = number * number
        # Add squared number to set
        squared_set.add(squared_number)
    return squared_set


def get_cubed_set():
    # declare variables
    cubed_set = set()

    # for loop to cube numbers in range 1-100
    for number in range(1, 101):
        # Calculate cubed values
        cubed_number = (number * number) * number
        # Add cubed number to set
        cubed_set.add(cubed_number)
    return cubed_set


def get_union():
    cubes = get_cubed_set()
    square = get_squared_set()

    # union two sets and assign to variable
    union_set = cubes | square
    return union_set


def get_intersection():
    cubes = get_cubed_set()
    square = get_squared_set()

    # intersect two sets and assign to variable
    intersection_set = cubes & square
    return intersection_set


def get_difference():
    cubes = get_cubed_set()
    square = get_squared_set()

    # difference two sets and assign to variable
    difference_set = cubes - square
    return difference_set


def main():
    # Declare loop variable to true
    run_loop = True

    # loop to run program until user exits
    while run_loop is True:
        # try/except statement to catch input errors
        try:
            selection = display_menu()

            if selection == 1:
                show_square_cube()
            elif selection == 2:
                try:
                    user_number = int(input("\nPlease enter an number: "))
                    show_square_cube(user_number)
                except ValueError:
                    print("\nIncorrect value entered. Please try again.")
            elif selection == 3:
                # run union function and print
                union_set = get_union()
                print("Union set:\n{}".format(union_set))
            elif selection == 4:
                # run intersection function and print
                intersection_set = get_intersection()
                print("Intersection set:\n{}".format(intersection_set))
            elif selection == 5:
                # run difference function and print
                difference_set = get_difference()
                print("Difference set:\n{}".format(difference_set))
            elif selection == 6:
                # set run_loop variable to False to exit loop
                run_loop = False
                # prints exit text
                print("\nThanks for using the Python Square & Cube Generator."
                      "\nGoodbye!")
            else:
                print("\nPlease try again.")
        except ValueError:
            print("\nIncorrect selection. Please try again.")


# runs main function
if __name__ == '__main__':
    main()
