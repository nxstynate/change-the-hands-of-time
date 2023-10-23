class FileCount:
    def file_count(self, input_directory, input_years, file_extensions=None):
        one_year_in_days = 365
        count = 0

        current_time = datetime.datetime.now()

        for root, _, files in os.walk(input_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_stat = os.stat(filepath)
                file_mtime = datetime.datetime.fromtimestamp(file_stat.st_mtime)

                # fix this logic right here because you need the file extension accounted for and the files that are two years or older acounted for do this wihtout haveing the conditional nested like chatgpt provided.

                if file_extensions is None or os.path.splitext(filename)[1] in file_extensions:
                    count += 1

                if (current_time - file_mtime).days > one_year_in_days * int(input_years):
                    count += 1

                else:
                    break

        return count
