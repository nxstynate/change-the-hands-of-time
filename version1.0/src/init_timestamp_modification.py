import os
import time
import datetime

class InitTimestampModification:
    def __init__(self, input_directory, input_years):
        self.one_year_in_seconds = 365 * 24 * 60 * 60
        self.current_time = time.time()
        self.input_directory = input_directory 
        self.input_years = input_years

    def timestamp_file_count(self):
        count = 0

        for root, _, files in os.walk(self.input_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                if (self.current_time - file_mtime.timestamp()) > (self.one_year_in_seconds * float(self.input_years)):
                    count += 1
                    print(f"\rNumber Of Files Found: {count}", end='', flush=True)
        print("\n")

        return count
    
    def timestamp_modification_file(self):
        count = 0

        for root, _, files in os.walk(self.input_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                if (self.current_time - file_mtime.timestamp()) > (self.one_year_in_seconds * float(self.input_years)):
                    os.utime(filepath, times=(self.current_time, self.current_time))
                    count += 1

        return count

    def timestamp_folder_count(self):
        count = 0 

        for root, _, _ in os.walk(self.input_directory):
            folder_stat = os.stat(root)
            folder_mtime = datetime.datetime.fromtimestamp(folder_stat.st_mtime)

            if (self.current_time - folder_mtime.timestamp()) > (self.one_year_in_seconds * float(self.input_years)):
                count += 1 
                print(f"\rNumber Of Folders Found: {count}", end='', flush=True)
        print("\n")

        return count

    def timestamp_modification_folder(self):
        count = 0

        for root, _, _ in os.walk(self.input_directory, topdown=False):
            folder_stat = os.stat(root)
            folder_mtime = datetime.datetime.fromtimestamp(folder_stat.st_mtime)

            if (self.current_time - folder_mtime.timestamp()) > (self.one_year_in_seconds * float(self.input_years)):
                os.utime(root, times=(self.current_time, self.current_time))

                parent_dir = os.path.dirname(root)
                if parent_dir:
                    os.utime(parent_dir, times=(self.current_time, self.current_time))
                count += 1

        return count
