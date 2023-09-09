#!/usr/bin/env python3

from openpyxl import Workbook, load_workbook

wb = load_workbook('/path/to/example.xlsx')

# Activate worksheet
ws = wb.active
print(ws)

# Get worksheet names
print(wb.sheetnames)

# Create worksheet
ws2 = wb.create_sheet("Sheet2")
ws2 = wb.create_sheet("Sheet2", 0) # Insert first
ws2 = wb.create_sheet("Sheet2", 1) # Insert last

# Access worksheet
ws2 = wb["Sheet2"]

# Delete worksheet
