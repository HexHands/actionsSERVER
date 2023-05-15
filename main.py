print("Script has been run!")
import time
import os
import sys
import time

# Define path to lock file
lock_file_path = "my_script.lock"

# Define maximum age of lock file in seconds
# Replace this with the maximum expected duration of your script
max_lock_file_age = 60 * 60  # 1 hour

# Check if lock file exists
if os.path.exists(lock_file_path):
    # Get age of lock file
    lock_file_age = time.time() - os.path.getmtime(lock_file_path)

    if lock_file_age < max_lock_file_age:
        print("Another instance of the script is already running. Exiting.")
        sys.exit(0)
    else:
        print("Found old lock file. Removing it and starting a new run.")

# Create or update lock file with current timestamp
with open(lock_file_path, "w") as lock_file:
    lock_file.write(str(time.time()))

# Run your script here
try:
    # Replace the following line with your script
    print("Running script...")
    start_time = time.time()

    while True:
      time.sleep(5)
      print(time.time() - start_time)
      if time.time() - start_time > 120:
        break

    print("Script has ended!")
    print(time.time() - start_time)

finally:
    # Remove lock file
    if os.path.exists(lock_file_path):
        os.remove(lock_file_path)
