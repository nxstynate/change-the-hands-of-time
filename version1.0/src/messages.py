class Messages:
    def invalid_choice_message(self):
        print("Invalid choice. Please select a valid option.\n")

    def invalid_path_message(self):
        print("Invalid path. Please enter a valid path.\n")

    def invalid_number_message(self):
        print("Invalid. Please enter a number.\n")

    def dotted_lines(self):
        print("\n................................................\n")

    def confirmation(self):
        while True:
            choice = input("""Enter 'y' for yes or enter 'n' for no:\n""").lower()

            if choice == 'y':
                return True

            elif choice == 'n':
                return False

            else:
                invalid_choice_message()
                dotted_lines()
