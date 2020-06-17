# Author: Justin Mullins
# Course: SDEV300
# Date: 14Jun2020
# Lab4

# import statements
import pandas as pd
import time
import re


def import_data():
    # declare/initialize variables
    input_data = []
    user_data = []

    # prints welcome/loading text
    print("Loading data into program, please wait...\n")

    # loads data file into program and appends each line to 'input_data' as list element
    with open("data.csv", "rt") as in_file:
        for line in in_file:
            line = line.split(',')
            input_data.append(line)

    # modifies 'input_data', assigns new variables and uses them to create a list
    # appends that list to empty list 'user_data'
    for element in input_data:
        first_name = element[0].strip().title()
        last_name = element[1].strip().title()
        phone_number = element[2].strip()
        zip_code = element[3].strip()
        user_data.append([first_name, last_name, phone_number, zip_code])

    # pauses for effect
    time.sleep(3)
    # print loading complete text
    print("Loading complete. Generating data log..\n")
    # pauses for effect
    time.sleep(2)

    # runs print_data function to display data frame
    print_data(user_data)


def print_data(user_data):
    # creates frame with column headers
    data_log = pd.DataFrame(user_data,
                            columns=["First Name", "Last Name", "Phone Number", "Zip Code"])

    # checks zip code formatting and overwrites column data with new values
    data_log["Zip Code"] = data_log["Zip Code"].map(get_formatted_zip)
    # checks phone number code formatting and overwrites column data with new values
    data_log["Phone Number"] = data_log["Phone Number"].map(get_formatted_phone)

    # runs function to check if data in a row needs to be reviewed
    needs_review(data_log)

    # prints output to screen
    print(data_log)


def get_formatted_zip(zip):
    # checks zip code value to see if it matches 5 digit template
    # if so returns the result else returns blank
    result = re.match(r'(\d{5})', zip)
    return "".join(result.groups()) if result else ""


def get_formatted_phone(number):
    # checks phone value to see if any match 10 digit template with dashes
    # returns the value if so
    for number in re.finditer(r'(\d{3})-(\d{3})-(\d{4})', number):
        if number:
            return '-'.join(number.groups())
    # if phone value doesn't match template with dashes runs 'else' code
    else:
        # checks phone value to see if it matches 10 digit template
        # if so returns the result else returns blank
        result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', number)
        return '-'.join(result.groups()) if result else ""


def needs_review(data_log):
    # declares/initializes variables
    column_list = []
    review_list = []
    count = 0

    # for loop to get header values and assign to list variable
    for item in data_log:
        column_list.append(item)

    # checks to see if any value in the row is blank
    # sets value accordingly and appends to review_list
    for index, row in data_log.iterrows():
        if (row[column_list[0]] == "" or row[column_list[1]] == "" or
                row[column_list[2]] == "" or row[column_list[3]] == ""):
            value = 'Y'
        else:
            value = 'N'
        review_list.append(value)

    # adds new column review to data frame
    data_log["Review?"] = review_list


# runs main function for program
if __name__ == '__main__':
    import_data()
