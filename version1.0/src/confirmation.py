class ConfirmationQuestions:

    def confirmation(self):

        while True:
            choice = input("""Enter 'y' for yes or enter 'n' for no:\n""").lower()

            if choice == 'y':
                return True

            elif choice == 'n':
                return False

            else:
                print("Invalid choice. Please select a valid option.\n")
                print(".............................................\n")
