import numpy as np
import matplotlib.pyplot as plt
from scipy import stats as st
'''

'''
def app(s1):
    n = int(input("Enter a number:"))
    
    print("Enter",n, " input values:")
    for i in range(0, n):
        x = int(input())
        s1.append(x)
yearsold = []
reads = []
app(yearsold)
app(reads)


slope, intercept, r, p, std_err = st.linregress(yearsold, reads)

def yin(x):
    return slope * x + intercept


yo = int(input("Enter age of your car:"))
print(yin(yo))
