import xlrd as xl
import matplotlib.pyplot as plt
from scipy import stats as st
loc = loc = ("E:\dataset01.xls")
wb = xl.open_workbook(loc)
sheet = wb.sheet_by_index(0)
x = []
y = []
print(sheet.ncols)
for j in range(0, 3):
    for i in range(sheet.nrows):
        if(j == 0 and i > 0):
            k = sheet.cell_value(i, j)
            x.append(k)
        elif(j == 1 and i > 0):
            k = sheet.cell_value(i, j)
            y.append(k)

slope, intercept, r, p, std_err = st.linregress(x, y)

def yin(x):
    return slope * x + intercept


yo = int(input("Enter a year:"))
print("A Predicted cost: ",yin(yo))
