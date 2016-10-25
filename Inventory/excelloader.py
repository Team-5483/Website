from openpyxl import Workbook
wb = Workbook()

ws = wb.active
ws['A1'] = 4
wb.save('test.xlsx')
