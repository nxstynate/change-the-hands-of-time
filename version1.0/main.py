from src.launch_powershell import LaunchPowershell
from src.display_menu import DisplayMenu
import os
import time
import datetime
import subprocess


class ChangeTheHandsOfTime:

    def main(self):
        display_menu = DisplayMenu()
        display_menu.display_menu()

if __name__ == "__main__":
    # init_powershell = LaunchPowershell()
    # init_powershell.main()
    init_program = ChangeTheHandsOfTime()
    init_program.main()


