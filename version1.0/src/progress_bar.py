import sys
import time

class ProgressBar:
    def progress_bar_finding_total(self, iterable, total, prefix='', length=50, fill='█'):
        def print_progress_bar(iteration):
            percent = ("{0:.1f}").format(100 * (iteration / float(total)))
            filled_length = int(length * iteration // total)
            bar = fill * filled_length + '-' * (length - filled_length)
            sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete')
            sys.stdout.flush()

        for i, item in enumerate(iterable):
            yield item
            print_progress_bar(i + 1)
        sys.stdout.write('\n')
        sys.stdout.flush()

    if __name__ == "__main__":
        total_items = 100  # Replace with your total number of items to process
        items_to_process = range(1, total_items + 1)

        for item in custom_progress_bar(items_to_process, total_items, prefix='Processing', length=50):
            # Simulate some work (replace this with your actual scan logic)
            time.sleep(0.1)

    def progress_bar_counting(self, iterable, total, prefix='', length=50, fill='█'):
        def print_progress_bar(iteration):
            percent = ("{0:.1f}").format(100 * (iteration / float(total)))
            filled_length = int(length * iteration // total)
            bar = fill * filled_length + '-' * (length - filled_length)
            sys.stdout.write(f'\r{prefix} |{bar}| {percent}% Complete')
            sys.stdout.flush()

        for i, item in enumerate(iterable):
            yield item
            print_progress_bar(i + 1)
        sys.stdout.write('\n')
        sys.stdout.flush()

    if __name__ == "__main__":
        total_items = 100  # Replace with your total number of items to process
        items_to_process = range(1, total_items + 1)

        for item in custom_progress_bar(items_to_process, total_items, prefix='Processing', length=50):
            # Simulate some work (replace this with your actual scan logic)
            time.sleep(0.1)

