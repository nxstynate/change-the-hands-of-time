from src.messages import Messages
from src.progress_bar import ProgressBar
from src.init_timestamp_modification import InitTimestampModification
import os
import time

class DisplayMenu:

    def display_menu(self):
        messages = Messages()
        progress_bar = ProgressBar()

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
                        change_time_stamp = InitTimestampModification(file_path, number)
                        number_of_files = change_time_stamp.timestamp_file_count()
                        number_of_folders = change_time_stamp.timestamp_folder_count()
                        print(f"You have {number_of_files} files and {number_of_folders} folders that are {number} years old.\n")
                        time.sleep(5)

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
                        change_time_stamp = InitTimestampModification(file_path, number)
                        number_of_files = change_time_stamp.timestamp_file_count()
                        number_of_folders = change_time_stamp.timestamp_folder_count()
                        print(f"You have {number_of_files} files and {number_of_folders} folders that are {number} years old.\n")
                        print(f"You are about to change the the timestamp on {number_of_files} files and {number_of_folders} folders.\nDo you want to continue?")

                        if messages.confirmation():
                            progress_bar.scan_items(number_of_files)
                            change_time_stamp.timestamp_modification_file()
                            change_time_stamp.timestamp_modification_folder()
                            print(f"\nConversion Completed:\n{file_path}")
                            messages.dotted_lines()
                            time.sleep(5)

                    except ValueError: 
                        messages.invalid_number_message()

                else: 
                    messages.invalid_path_message()


            elif choice == '3':
                print("Are you sure you want to quit?\n")
                if messages.confirmation():
                    return
                messages.dotted_lines()

            else: 
                messages.invalid_choice_message()
                messages.dotted_lines()

