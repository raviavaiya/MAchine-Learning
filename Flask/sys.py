import sys

# Open the file in write mode
log_file = open('api_logs.txt', 'w')

# Redirect stdout to the file
sys.stdout = log_file

# Example logs
print("API request received.")
print("Processing the request.")
print("Response sent.")

# Close the file after writing
log_file.close()

# Revert stdout to normal (optional)
sys.stdout = sys.__stdout__
