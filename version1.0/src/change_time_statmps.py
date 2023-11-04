import os
import time
import datetime

class ChangeTimeStamps:
    def change_time_stamp(self, input_directory, input_years):
        one_year_in_days = 365
        count = 0

        current_time = datetime.datetime.now()

        for root, _, files in os.walk(input_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                if (current_time - file_mtime).days > one_year_in_days * float(input_years):
                    os.utime(filepath, times=(current_time.timestamp(), current_time.timestamp()))
                    count += 1
                    print(f"\rNumber Of Files Found: {count}", end='', flush=True)
                else:
                    break

