#!/usr/bin/env python3

from openpyxl import Workbook, load_workbook

# Create workbook
wb = Workbook()
ws = wb.active

# Open workbook
wb = load_workbook('/path/to/file.xlsx')
ws = wb.active

# Activate workbook
ws = wb["Sheet2"]

# Save workbook
wb.save(filename = "file.xlsx")
