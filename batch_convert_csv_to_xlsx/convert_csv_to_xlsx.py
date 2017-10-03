import os
import glob
import csv
import openpyxl # from https://pythonhosted.org/openpyxl/ or PyPI (e.g. via pip)

#Credit goes to https://superuser.com/questions/301431/how-to-batch-convert-csv-to-xls-xlsx
for csvfile in glob.glob(os.path.join('.', '*.csv')):

	wb = openpyxl.Workbook()
	ws = wb.active

	with open(csvfile, 'r') as f:
		reader = csv.reader(f)
		for r, row in enumerate(reader, start=1):
			for c, val in enumerate(row, start=1):
				ws.cell(row=r, column=c).value = val
	wb.save(csvfile + '.xlsx')