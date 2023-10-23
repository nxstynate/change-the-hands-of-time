
class ConfirmationQuestions:

    def confirmation(self):
        display_menu = ChangeTheHandsOfTime()
        
        while True:
            choice = input("""Enter 'y' for yes or enter 'n' for no:\n""")

            if choice == 'n':
                return null

            elif choice == 'y':
                break

            else:
                print("Invalid choice. Please select a valid option.")
