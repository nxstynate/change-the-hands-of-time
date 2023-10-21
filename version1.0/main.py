import os
import time
import datetime

class ChangeTheHandsOfTime:

    def file_count(self, directory):
        count = 0
        current_time = datetime.datetime.now()

        for root, _, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                # count += 1

                # Check if the file is older than 2 years
                if (current_time - file_mtime).days > 1:
                    # 365 days/year * 2 years + a buffer
                    # os.utime(filepath, times=(current_time.timestamp(), current_time.timestamp()))
                    count += 1

        return count


    def change_time_stamp(self, input_path):
        files = os.listdir(input_path)

        for file_name in files:
            file_path = os.path.join(input_path, file_name)
            new_timestamp = time.time()
            os.utime(file_path, (new_timestamp, new_timestamp))


    def display_menu(self):
        while True:
            print("Hands of Time:\n1. Scan\n2. Run\n3. Quit\n")

            choice = input("Enter your choice:\n")

            if choice == '1': 
                file_path = input("Enter path to folder:\n")
                print(f"You have {self.file_count(file_path)} files.")
                break

            elif choice == '2':
                file_path = input("Enter path to folder:\n")
                print(f"You have {self.file_count(file_path)} files.")
                self.change_time_stamp(file_path)
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

def main():
    init_program = ChangeTheHandsOfTime()
    init_program.display_menu()

if __name__ == "__main__":
    main()
