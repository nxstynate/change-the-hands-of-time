from tqdm import tqdm
import time

class ProgressBar: 
    def scan_items(self, total_items):
        # Create a tqdm progress bar with the specified total_items
        progress_bar = tqdm(total=total_items, unit="item")

        for item in range(1, total_items + 1):
            # Simulate some work (replace this with your actual scan logic)
            time.sleep(0.1)

            # Update the progress bar
            progress_bar.update(1)
            progress_bar.set_description(f"Updating Timestamps: {item}/{total_items}")

        # Close the progress bar when done
        progress_bar.close()

    if __name__ == "__main__":
        total_items = 100  # Replace with your total number of items to scan
        scan_items(total_items)

