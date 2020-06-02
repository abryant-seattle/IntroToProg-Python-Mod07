# ------------------------------------------------- #
# Title: Assignment07
# Description: Demonstrating Pickling and Structured Error Handling
# ChangeLog: (When, Who, What)
# 2020-05-29, Alexander Bryant, Created Script and function outlines
# 2020-05-30, Alexander Bryant, Generalized functions and added to Processor Class
# 2020-05-31, Alexander Bryant, Added docstrings for functions and revised function / variable names for consistency
# 2020-06-01, Alexander Bryant, Reviewed print statements for consistency and prepared code for demonstration
# ------------------------------------------------- #

# Data -------------------------------------------- #
import pickle  # Imports the pickling module

menu_input = 0  # Captures the user's menu choice


# # Processing -------------------------------------- #
class Processor:
    """The processor class handles the mechanics of requesting, saving, and retrieving saved contacts"""

    @staticmethod
    def request_info():
        """request_info asks the user for contact information, including the name, company, and job title of
         the contact and assigns them as lower case string local variables. These variables are then plugged into the
         save_info function parameters. This function has no associated parameters."""
        name_input = str(input('Please enter contact name: ')).lower()
        company_input = str(input('Please enter contact company: ')).lower()
        title_input = str(input('Please enter contact job title: ')).lower()
        Processor.save_info(name=name_input, company=company_input, title=title_input)
        return

    @staticmethod
    def save_info(name, company, title):
        """save_info takes the data entered in the request_info function, adds it to a list object, and then pickles
        the information. This data is saved (dumped) as a binary dat file named after the contact. The parameters name,
        company, and title correspond to the variables created in the request_info function."""
        info_list = [[name, company, title]]
        active_file = open(str(name + '.dat'), 'wb')
        pickle.dump(info_list, active_file)
        active_file.close()
        print('Contact "' + str(name).title() + '" has been saved.')
        return

    @staticmethod
    def review_info():
        """review_info allows the user to view saved contacts by prompting the user to supply a contact name. The
        function then attempts to open a binary dat file under that name. An error handling block in the presentation
        prevents the script from crashing if no file by that name is found. When a file is found, the file is read
        (load) and a for loop prints the contents in title case. This function has no associated parameters."""
        file_name = str(input('Enter Contact Name: ')).lower()
        active_file = open(str(file_name + '.dat'), 'rb')
        for i in pickle.load(active_file):
            print('\nName: ' + i[0].title())
            print('Company: ' + i[1].title())
            print('Job Title: ' + i[2].title())
        return


# Presentation ------------------------------------ #

input('Press enter to begin: \n')
while True:

    print('\n***Menu Options*** \n\n 1 - Add a new contact \n 2 - Find an existing contact \n 3 - Quit \n')

    try:  # This try error block prevents a crash if the user selects an invalid menu option
        menu_input = int(input('Please select a menu option: '))

        if menu_input == int(1):
            Processor.request_info()

        elif menu_input == int(2):
            try:  # This try error block prevents a crash if no file with the supplied name is found
                Processor.review_info()
            except FileNotFoundError as e:
                print('\nOops! File not found!')
                print('No contact file matches that name as entered.')
                print('Please check the spelling of that name or add a new contact. \n')

        elif menu_input == int(3):
            break

        else:
            print('\nInvalid selection, please select a valid menu option.\n')

    except ValueError as e:
        print('\nInvalid selection, please try a valid menu option.\n')
