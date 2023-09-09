# Dictionary reader

import csv

with open('file.csv', 'r') as file:
  csv_reader = csv.DictReader(file)

  with open('new_file.csv', 'w',) as new_file:
    # Specify fieldnames
    fieldnames = ['first name', 'last_name', 'email']
    # Initialize
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
    # Write header
    csv_writer.writeheader()

    for line in csv_reader:
      # Delete line
      del line['email']
      csv_writer.writerow(line)
