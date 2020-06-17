# Author: Justin Mullins
# Class: SDEV300
# Date: 8JUNE20

# import modules
import json


def display_menu():
    # creates display menu
    print("\n**STATES MENU**",
          "\n1. Display U.S. States, state flower and state capitol",
          "\n2. Search for state",
          "\n3. Update a state bird",
          "\n4. Exit program")

    # get user input and assing to 'user_input'
    user_input = int(input("\nChoose a selection from the above menu (1,2,3 or 4):"))
    return user_input


# loads dictionary from json file and saves it to 'data' variable
def load_json():
    with open("states.json", 'r') as json_file:
        data = json.load(json_file)
    return data


# saves changes to json file
def save_json(data):
    with open("states.json", "w") as out_file:
        json.dump(data, out_file, indent=4, sort_keys=True)


# display states, state capital and flower
def display_states():
    # calls load_json function saves it to 'data'
    data = load_json()

    # for loop to iterate through json file for each element in dictionary list
    for item in data["States"]:
        for state in item.keys():
            state_name = state
            state_data = item[state]
        # for loop that iterates through each element to get
        # state capital and flower for each state and assigns to variables
        for thing in state_data:
            for value in thing.keys():
                if value == "Capital":
                    state_capital = thing[value]
                elif value == "State Flower":
                    state_flower = thing[value]
        # prints state, state capital and flower
        print("\nState: {}".format(state_name),
              "\nCapital: {}".format(state_capital),
              "\nFlower: {}".format(state_flower))


def state_search():
    # user input to get state searched for and assign it to variable 'user_search'
    user_search = input("Please enter a state name to search for:")

    # load json file
    data = load_json()

    # for loop to iterate through json file and find specific state
    for item in data["States"]:
        # for loop to get dictionary keys
        for state in item.keys():
            # turns state  and user_search values to lowercase to see if string matches
            if state.lower() == user_search.lower().strip():
                state_data = item[state]
                # if state is found sets boolean value to True
                # and breaks out of second for loop
                state_exists = True
                break
            else:
                # sets value to false if state is not found
                state_exists = False
        # breaks out of first for loop if state is found
        if state_exists is True:
            break

    # if state exists, get state bird and capital
    if state_exists:
        for element in state_data:
            for value in element.keys():
                if value == "State Bird":
                    s_bird = element[value]
                elif value == "Capital":
                    s_cap = element[value]
        # print state searched, capital and bird
        print("\nState Searched: {}"
              "\nState Capital: {}"
              "\nState Bird: {}".format(user_search.capitalize(), s_cap, s_bird))
    # prints if state is not found
    else:
        print("State not found. Please try again.")


def update_state():
    # user input to get state searched for and assign it to variable 'state_input'
    state_input = input("\nPlease enter a state name to search for:")
    # user input to get new bird name
    bird_input = input("\nPlease enter a new state bird:")
    # load json file
    data = load_json()

    for item in data["States"]:
        for element in item.keys():
            if element.lower() == state_input.lower():
                state_data = item[element]
                state_exists = True
                break
            else:
                state_exists = False
        if state_exists is True:
            break

    if state_exists is True:
        for thing in state_data:
            for key in thing.keys():
                if key == "State Bird":
                    old_bird = thing[key].lower().capitalize()
                    new_bird = bird_input.lower().capitalize()
                    thing[key] = new_bird
                else:
                    pass
        save_json(data)
        print("\nUpdated state bird for {}:"
              "\nOld State Bird: {}"
              "\nNew State Bird: {}".format(element, old_bird, new_bird))
    else:
        print("State not found. Please try again.")


def main():
    # variable 'run_loop' set to True to keep loop running
    run_loop = True

    print("\nWelcome to the Python States Application!")

    # loop to run program until user exits
    while run_loop:
        try:
            selection = display_menu()

            if selection == 1:
                # runs display_states() function
                display_states()
            elif selection == 2:
                # runs state_search() function
                state_search()
            elif selection == 3:
                # runs update_state() function
                update_state()
            elif selection == 4:
                # prints exit statement and exits program
                print("\nThanks for using the Python State Application!")
                run_loop = False

        except ValueError:
            print("Incorrect selection, please try again.")


if __name__ == '__main__':
    main()
