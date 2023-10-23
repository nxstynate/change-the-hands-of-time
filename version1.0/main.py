import os
import time
import datetime
import subprocess
from src.confirmation import ConfirmationQuestions
from src.file_count import FileCount
from src.change_time_statmps import ChangeTimeStamps
from src.launch_powershell import LaunchPowershell

class ChangeTheHandsOfTime:


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
                print(f"You have {file_count.file_count(file_path, number_of_years)} files.")
                break

            elif choice == '2':
                file_path = input("Enter path to folder:\n")
                number_of_years = input("Enter number of years:\n")
                print(f"You have {file_count.file_count(file_path, number_of_years)} files.")
                change_time_stamps.change_time_stamp(file_path, number_of_years)
                print(f"Conversion Completed:\n{file_path}")
                break

            elif choice == '3':
                print("Are you sure you want to quit?\n")
                confirmation.confirmation()
                break

            else:
                print("Invalid choice. Please select a valid option.")


    def main(self):
        self.display_menu()


if __name__ == "__main__":
    # init_powershell = LaunchPowershell()
    # init_powershell.main()
    init_program = ChangeTheHandsOfTime()
    init_program.main()


