from src.invalid_choice_message import InvalidChoice

class ConfirmationQuestions:

    def confirmation(self):
        invalid_message = InvalidChoice()

        while True:
            choice = input("""Enter 'y' for yes or enter 'n' for no:\n""").lower()

            if choice == 'y':
                return True

            elif choice == 'n':
                return False

            else:
                invalid_message.invalid_choice_message()
                print(".............................................\n")
