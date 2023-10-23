import os
import time
import datetime
import subprocess

class LaunchPowershell: 

    def openPowershell(self):
        # target_script = 
        # powershell_command = f"powershell.exe -Execution Policy Bypass -File {target_script}"
        open_powershell_command = f"powershell.exe"
        subprocess.run(open_powershell_command, shell=True)

    def main(self):
        self.openPowershell()



class ChangeTheHandsOfTime:

    def file_count(self, input_directory, input_years):
        one_year_in_days = 365
        count = 0

        current_time = datetime.datetime.now()

        for root, _, files in os.walk(input_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                if (current_time - file_mtime).days > one_year_in_days * int(input_years):
                    count += 1
                else:
                    break

        return count


    def change_time_stamp(self, input_directory, input_years):
        one_year_in_days = 365
        count = 0

        current_time = datetime.datetime.now()

        for root, _, files in os.walk(input_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                if (current_time - file_mtime).days > one_year_in_days * int(input_years):
                    os.utime(filepath, times=(current_time.timestamp(), current_time.timestamp()))
                    count += 1
                else:
                    break


    def display_menu(self):
        while True:
            print("Hands of Time:\n1. Scan\n2. Run\n3. Quit\n")

            choice = input("Enter your choice:\n")

            if choice == '1': 
                file_path = input("Enter path to folder:\n")
                number_of_years = input("Enter number of years:\n")
                print(f"You have {self.file_count(file_path, number_of_years)} files.")
                break

            elif choice == '2':
                file_path = input("Enter path to folder:\n")
                number_of_years = input("Enter number of years:\n")
                print(f"You have {self.file_count(file_path, number_of_years)} files.")
                self.change_time_stamp(file_path, number_of_years)
                print(f"Conversion Completed:\n{file_path}")
                break

            elif choice == '3':
                print("Are you sure you want to quit?\n")
                self.confirmation()
                break

            else:
                print("Invalid choice. Please select a valid option.")


    def confirmation(self):
        while True:
            choice = input("""Enter 'y' for yes or enter 'n' for no:\n""")

            if choice == 'n':
                self.display_menu()

            elif choice == 'y':
                break

            else:
                print("Invalid choice. Please select a valid option.")


    def main(self):
        self.display_menu()


if __name__ == "__main__":
    init_powershell = LaunchPowershell() 
    init_powershell.main()
    init_program = ChangeTheHandsOfTime()
    init_program.main()


