import openpyxl

wb = openpyxl.load_workbook('example2.xlsx')

sheet = wb['Sheet1']

for i in range(1, 11):
    sheet['A' + str(i)] = 'test'

wb.save('example2.xlsx')


