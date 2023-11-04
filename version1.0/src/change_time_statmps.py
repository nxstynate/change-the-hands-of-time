import os
import time
import datetime

class ChangeTimeStamps:
    def change_time_stamp(self, input_directory, input_years):
        one_year_in_seconds = 365 * 24 * 60 * 60
        count = 0

        current_time = time.time()

        for root, _, files in os.walk(input_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                if (current_time - file_mtime.timestamp()) > (one_year_in_seconds * float(input_years)):
                    print('hello world')
                    os.utime(filepath, times=(current_time, current_time))
                    count += 1

