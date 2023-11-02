from src.confirmation import ConfirmationQuestions
from src.file_count import FileCount
from src.change_time_statmps import ChangeTimeStamps
from src.invalid_choice_message import InvalidChoice
import os
import time
import datetime

class DisplayMenu:

    def display_menu(self):
        confirmation = ConfirmationQuestions()
        file_count = FileCount()
        change_time_stamps = ChangeTimeStamps()
        invalid_message = InvalidChoice()

        while True:
            print("Hands of Time:\n1. Scan\n2. Run\n3. Quit\n")

            choice = input("Enter your choice:\n")

            if choice == '1': 
                file_path = input("Enter path to folder:\n")
                if os.path.exists(file_path):
                    number_of_years = input("Enter number of years:\n")
                    if number_of_years.isdigit():
                        print(f"You have {file_count.file_count(file_path, number_of_years)} files and {file_count.folder_count(file_path, number_of_years)} folders that are {number_of_years} years old.\n")
                        
                    else: 
                        invalid_message.invalid_number_message()

                else: 
                    invalid_message.invalid_path_message()

            elif choice == '2':
                file_path = input("Enter path to folder:\n")
                if os.path.exists(file_path):
                    number_of_years = input("Enter number of years:\n")
                    if number_of_years.isdigit():

                        number_of_files = file_count.file_count(file_path, number_of_years)
                        print(f"You have {number_of_files} files that are {number_of_years} years old.\n")
                        print(f"You are about to change the the timestamp on {number_of_files} files.\nDo you want to continue?")

                        if confirmation.confirmation():
                            change_time_stamps.change_time_stamp(file_path, number_of_years)
                            print(f"Conversion Completed:\n{file_path}")
                            print(".............................................\n")

                    else: 
                        invalid_message.invalid_number_message()

                else: 
                    invalid_message.invalid_path_message()


            elif choice == '3':
                print("Are you sure you want to quit?\n")
                if confirmation.confirmation():
                    return
                print(".............................................\n")

            else: 
                invalid_message.invalid_choice_message()
                print(".............................................\n")
