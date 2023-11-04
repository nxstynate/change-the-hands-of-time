from src.launch_powershell import LaunchPowershell
from src.display_menu import DisplayMenu
import os
import time
import datetime
import subprocess

# need to fix the actual conversion of files, at the moment the files do not get their tmestamps chagned.
# work on the change_time_stamps module to fix this issue.


class ChangeTheHandsOfTime:

    def main(self):
        display_menu = DisplayMenu()
        display_menu.display_menu()

if __name__ == "__main__":
    # init_powershell = LaunchPowershell()
    # init_powershell.main()
    init_program = ChangeTheHandsOfTime()
    init_program.main()


