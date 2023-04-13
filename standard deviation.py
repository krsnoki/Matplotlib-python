import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

s1 = [45, 65, 89, 75, 78, 21, 15]
s2 = [52, 65, 45, 48, 49, 39, 46]
s3 = [89, 89, 89, 89, 89, 89, 89]
s4 = [11, 12, 13, 14, 15, 16, 17]
s5 = [11, 12, 13, 14, 15, 16, 17]


l = [s1, s2, s3, s4]
d = []
for i in range(1, 4):
    k = np.std(l[i])
    d.append(k)

o = 0
k = d[0]
for i in d:
    if(i < k):
        k = i
        c = o
    o = o + 1

print("Age group of set",c," have similar ages")
'''
if(d1 < d2 and d1 < d3 and d1 < d4):
    print("Age group of set 1 have similar ages")
elif(d2 < d3 and d2 < d4):
    print("Age group of set 2 have similar ages")
elif(d3 < d4):
    print("Age group of set 3 have similar ages")
else:
    print("Age group of set 4 have similar ages")

'''
