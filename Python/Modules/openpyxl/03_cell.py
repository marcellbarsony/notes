#!/usr/bin/env python3

from openpyxl import Workbook, load_workbook

wb = load_workbook('/path/to/example.xlsx')
wb = load_workbook('example.xlsx')
ws = wb.active

# Access single cell
c = ws['C3']
c = ws.cell(row=3, column=3, value=10)

# Access many cells
c = ws['A1':'C3']

# Access columns & rows
colC = ws['C']
col_range = ws['C':'D']
row10 = ws[10]
row_range = ws[5:10]

# Iterate rows
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cells in row:
        print(cells)

# Iterate columns
for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
    for cell in col:
        print(cell)


