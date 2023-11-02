from src.confirmation import ConfirmationQuestions
from src.file_count import FileCount
from src.change_time_statmps import ChangeTimeStamps
import os
import time
import datetime

class DisplayMenu:

    def display_menu(self):
        confirmation = ConfirmationQuestions()
        file_count = FileCount()
        change_time_stamps = ChangeTimeStamps()

        while True:
            print("Hands of Time:\n1. Scan\n2. Run\n3. Quit\n")

            choice = input("Enter your choice:\n")

            if choice == '1': 
                file_path = input("Enter path to folder:\n")
                number_of_years = input("Enter number of years:\n")
                print(f"You have {file_count.file_count(file_path, number_of_years)} files that are {number_of_years} years old.\n")

            elif choice == '2':
                file_path = input("Enter path to folder:\n")
                number_of_years = input("Enter number of years:\n")
                number_of_files = file_count.file_count(file_path, number_of_years)
                print(f"You have {number_of_files} files that are {number_of_years} years old.\n")
                print(f"You are about to change the the timestamp on {number_of_files} files.\nDo you want to continue?")

                if confirmation.confirmation():
                    return

                elif confirmation.confirmation() == True: 
                    change_time_stamps.change_time_stamp(file_path, number_of_years)
                    print(f"Conversion Completed:\n{file_path}")
                    #fix the logic in this elif conditional at the moment it's not working. i need it to be able to ask if the user wants to cointue to proceed to convert the files if they choose yes it'll proceed with the conversion process via the function if no the the program will start over at the begining.


            elif choice == '3':
                print("Are you sure you want to quit?\n")
                if confirmation.confirmation():
                    return
                print(".............................................\n")

            else: 
                print("Invalid choice. Please select a valid option.\n")
                print(".............................................\n")
