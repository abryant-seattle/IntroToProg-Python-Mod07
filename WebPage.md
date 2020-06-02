Alexander Bryant
6/1/2020
Foundations of Programming
Assignment 07

# Pickling Contacts

### Intro
This week’s module focused on both pickling functions and error handling within Python. This week’s assignment was to
create a script that demonstrated the usage of pickling and error handling. I chose to write a script that creates,
saves, and reviews contact information, with a few deliberate choices made to demonstrate error handling.

### Process
Keeping up with separation of concerns, this script is split into data, processing, and presentation sections.
Within the data section, the pickle module is imported and the lone global variable is declared. The variable
menu_input captures the user’s menu choice as an integer in the main body of the script. Next, the processing section
contains the definitions for functions within the Processor class.

![fig 1](https://github.com/abryant-seattle/IntroToProg-Python-Mod07/blob/master/fig1.JPG "Figure 1")

**_Figure 1: The request_info function requests contact info from the user._**

In Figure 1 above, the request_info function is defined as a method within the Processor class. Three input statements
request a contact name, company, and job title, which are interpreted as lower case strings and assigned to the local
variables name_input, company_input, and title_input. The function then inserts the local variables as the keyword
arguments name, company, and title into another function, save_info.

![fig 2](https://github.com/abryant-seattle/IntroToProg-Python-Mod07/blob/master/fig2.JPG "Figure 2")

**_Figure 2: The save_info function saves data from the request_info function as a dat file._**

In Figure 2 above, the save_info function is defined as a method within the Processor class. The parameters name,
company, and title are supplied by the request_info function. The data is added to a list and a new binary file is
created with a naming convention based on the name parameter. The pickle function then saves (dumps) the list to the
new file, and then closes the file for later review. A confirmation message is printed for the user to let them know
the contact has been saved.

![fig 3](https://github.com/abryant-seattle/IntroToProg-Python-Mod07/blob/master/fig3.JPG "Figure 3")

**_Figure 3: In PyCharm, the user adds a new contact’s name, company, and title._**

In Figure 3 above, a PyCharm user selects menu option 1 and adds new contact information. Behind the scenes, the
request_info function collects the contact information and passes it along to the save_info function, which creates a
binary file based on the contact name.

![fig 4](https://github.com/abryant-seattle/IntroToProg-Python-Mod07/blob/master/fig4.JPG "Figure 4")

**_Figure 4: The review_info function retrieves saved contact files._**

In Figure 4 above, the review_info function is defined as a method within the Processor class. A prompt asks the user
to supply a contact name which is interpreted as a lowercase string and assigned to the local variable file_name. The
script then attempts to open a binary file based on the name provided by the user. An error handling block in the body
of the script is activated if no file matching the supplied name is found.

![fig 5](https://github.com/abryant-seattle/IntroToProg-Python-Mod07/blob/master/fig5.JPG "Figure 5")

**_Figure 5: If no matching file is found by the review_info function an error message prints._**

In Figure 5 above, a try-except block prevents the code from crashing due to a FileNotFoundError. Because the
review_info and save_info take user input as lowercase strings, case does not need to match a saved file, but
characters and spacing does.

![fig 6](https://github.com/abryant-seattle/IntroToProg-Python-Mod07/blob/master/fig6.JPG "Figure 6")

**_Figure 6: A command line user causes an error due to spelling mistakes_**

In Figure 6 above, a command line user runs the program and looks for the contact saved earlier, but makes several
spelling mistakes. The try-except block prevents the code from crashing due to an error and reminds the user to check
the spelling. The user then tries again with the correct spelling, but this time in uppercase to reflect annoyance.
The review_info function finds the correct file due to the correct characters and spacing, while ignoring the
capitalization.

![fig 7](https://github.com/abryant-seattle/IntroToProg-Python-Mod07/blob/master/fig7.JPG "Figure 7")

**_Figure 7: The presentation block houses the menu in a while loop and try-except block._**

The body of the script is in the presentation block, visible above in Figure 7. After pressing enter to begin the program, a menu is presented
inside of a while loop. A try-except block ensures that the program does not crash if the user selects an invalid
selection. Typically I would specify menu options as strings and compare them against a list of appropriate options.
However, I specified the variable menu_input as an integer to test catching another type of error, the ValueError.
If the user submits an integer other than 1, 2, or 3, an else statement reminds the user to pick another option.
But, if the user submits an entry that can’t be interpreted as an integer, such as ‘1.0’ or ‘three’, then the except
statement catches the ValueError. Instead of crashing the program, the user is reminded to select a valid option and
is returned to the menu. In Figure 8 below, the command line user mistakes the program for a drive thru window and
submits string characters that cannot be interpreted as an integer. Instead of crashing, the user is warned that this
is an invalid selection and returned to the menu.

![fig 8](https://github.com/abryant-seattle/IntroToProg-Python-Mod07/blob/master/fig8.JPG "Figure 8")

**_Figure 8: When menu_option is not an integer, a try-except block prevents a script crash._**

###Summary
Pickling presents an alternative method of writing and reading files within Python. While these small pieces of contact information do not take up very much space, binary files can compress much larger objects into smaller pieces of information. The most difficult portion of this project was devising a concept program to illustrate pickling and error handling. I chose to model the program after the modest Rolodex, knowing a name would allow the user to look up more information about that contact. This code would function more similar to a Rolodex or phonebook if an additional menu item would allow the user to review all of the names which had been added. For the sake of simplicity to focus on pickling and error handling, I omitted the phonebook feature. Another difficult aspect of this assignment was pre-empting the various types of errors that a user could make that would trigger the code to crash. More extensive testing would likely illustrate a use for try-except blocks in other locations within the script.
