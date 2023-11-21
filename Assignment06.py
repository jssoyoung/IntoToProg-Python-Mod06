# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
# Jessica Yun, 11/16/2023, Created Script
# Jessica Yun, 11/17/2023, Wrote code
# Jessica Yun, 11/20/2023, Debugged code
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = 'Enrollments.json'
students: list = []  # a table of student data
menu_choice = ''

# Processing --------------------------------------- #
class FileProcessor:
    # When the program starts, read the file data into table
    # Extract the data from the file
    # Read from the Json file
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        '''
        The function reads JSON information from the specified file
        :param file_name: A string indicating the file name
        :return:The student data which is of type list[dict[str, str | float]]
        '''
        try:
            file = open(FILE_NAME, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        '''
        The function writes JSON information into the specified file
        :param student_data: The roster to add to
        '''
        try:
            file = open(FILE_NAME, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        '''
        Prints an error message to the user
        :param message: The message to print
        :param exception: The exception for the error
        :return: The error message
        '''
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        '''
        Displays the menu options for the user
        :param menu: The string with the menu options
        :return: The user's string choice from 1, 2, 3, 4
        '''
        print()
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user
        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        '''Displays information regarding students
        :param student_data: The roster of students
        '''
        # Process the data to create and display a custom message
        print()
        print("-" * 50)
        for student_data in students:
            print(f'Student {student_data["FirstName"]} '
                  f'{student_data["LastName"]} is enrolled in {student_data["CourseName"]}')
        print("-" * 50)
        print()

    @staticmethod
    def input_student_data(student_data: list):
        '''
        Retrieves information required for each student including first name, last name, and course name
        :param student_data: The roster to add to
        :return: The roster
        '''
        try:
            # Input the data
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

#  End of function definitions


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    # Input user data
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "2":  # Display current data
        IO.output_student_courses(student_data=students)  # Added this to improve user experience
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop

    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
