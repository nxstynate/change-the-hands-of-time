import os
import time
import datetime

class FileCount:
    def __init__(self):
        self.one_year_in_days = 365
        self.current_time = datetime.datetime.now()

    def file_count(self, input_directory, input_years, file_extensions=None):
        count = 0

        for root, _, files in os.walk(input_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                if file_extensions is None or os.path.splitext(filename)[1] in file_extensions:
                    count += 1

                if (self.current_time - file_mtime).days > self.one_year_in_days * int(input_years):
                    count += 1

                else:
                    break

        return count


    def folder_count(self,input_directory, input_years):
        count = 0 

        for root, _, _ in os.walk(input_directory):
            folder_stat = os.stat(root)
            folder_mtime = datetime.datetime.fromtimestamp(folder_stat.st_mtime)

            if (self.current_time - folder_mtime).days > self.one_year_in_days * int(input_years):
                count += 1 
        return count
