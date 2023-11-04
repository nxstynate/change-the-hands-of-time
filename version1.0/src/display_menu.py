from src.confirmation import ConfirmationQuestions
from src.file_count import FileCount
from src.change_time_statmps import ChangeTimeStamps
from src.messages import Messages
import os
import time
import datetime

class DisplayMenu:

    def display_menu(self):
        confirmation = ConfirmationQuestions()
        file_count = FileCount()
        change_time_stamps = ChangeTimeStamps()
        messages = Messages()

        while True:
            messages.dotted_lines()
            print("Hands of Time:\n1. Scan\n2. Run\n3. Quit\n")

            choice = input("Enter your choice:\n")

            if choice == '1': 
                file_path = input("Enter path to folder:\n")
                if os.path.exists(file_path):
                    number_of_years = input("Enter number of years:\n")
                    try: 
                        number = float(number_of_years)
                        print(f"\nYou have {file_count.file_count(file_path, number)} files and {file_count.folder_count(file_path, number)} folders that are {number} years old.\n")

                    except ValueError:
                        messages.invalid_number_message()

                else: 
                    messages.invalid_path_message()

            elif choice == '2':
                file_path = input("Enter path to folder:\n")
                if os.path.exists(file_path):
                    number_of_years = input("Enter number of years:\n")
                    try: 
                        number = float(number_of_years)

                        number_of_files = file_count.file_count(file_path, number_of_years)
                        print(f"\nYou have {number_of_files} files that are {number_of_years} years old.\n")
                        print(f"You are about to change the the timestamp on {number_of_files} files.\nDo you want to continue?")

                        if confirmation.confirmation():
                            change_time_stamps.change_time_stamp(file_path, number_of_years)
                            print(f"Conversion Completed:\n{file_path}")
                            messages.dotted_lines()

                    except ValueError: 
                        messages.invalid_number_message()

                else: 
                    messages.invalid_path_message()


            elif choice == '3':
                print("Are you sure you want to quit?\n")
                if confirmation.confirmation():
                    return
                messages.dotted_lines()

            else: 
                messages.invalid_choice_message()
                messages.dotted_lines()

