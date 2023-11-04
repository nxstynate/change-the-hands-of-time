from src.messages import Messages

class ConfirmationQuestions:

    def confirmation(self):
        messages = Messages()

        while True:
            choice = input("""Enter 'y' for yes or enter 'n' for no:\n""").lower()

            if choice == 'y':
                return True

            elif choice == 'n':
                return False

            else:
                messages.invalid_choice_message()
                messages.dotted_lines()
