import subprocess

class LaunchPowershell:

    def openPowershell(self):
        # target_script =
        # powershell_command = f"powershell.exe -Execution Policy Bypass -File {target_script}"
        open_powershell_command = f"powershell.exe"
        subprocess.run(open_powershell_command, shell=True)

    def main(self):
        self.openPowershell()
