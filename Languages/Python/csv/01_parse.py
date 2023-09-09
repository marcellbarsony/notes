# Parse csv files

import csv

# Read csv
with open('file.csv', 'r') as file:
  csv_reader = csv.reader(file, delimiter=',')

  # Skip 1st line
  next(csv_reader)

  # Iterate lines
  for line in csv_reader:
    # Print 2nd index
    print(line[2])

# Create new file
with open('new_names.csv', 'w') as new_file:
  csv_writer = csv.writer(new_file, delimiter='\t')

  # Write to new file
  for line in csv_writer:
    csv_writer.writerow(line)
