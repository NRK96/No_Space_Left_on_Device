import os.path
import sys

current_directory = os.path.dirname(os.path.realpath(__file__))

# Setup variables for future computation.
filepath = current_directory + '\\Resources\\Sample.txt'

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

for line in lines:
    print(line)

file.close()
