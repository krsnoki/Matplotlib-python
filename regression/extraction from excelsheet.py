import xlrd as xl
loc = ("E:\dataset01.xls")
wb = xl.open_workbook(loc)
sheet = wb.sheet_by_index(0)
print(sheet.nrows)
for j in range(3):
    for i in range(4):
        print(sheet.cell_value(i, j))
    print("")
   
