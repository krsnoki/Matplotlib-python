from numpy import random as rd
import numpy as np
from matplotlib import pyplot as pt
#take arra1 with range from 1 to 6 total 100 elements
#array2 with range 1 to 6


x = np.array([1, 2, 3, 4, 5, 6])
y = rd.randint(6, size = (100))
y1 = rd.randint(6, size = (100))

c = []
c1 = []
for i in range(100):
    if(y[i] == 1):
        c[i]
    elif(y[i] == 2):
        two = two + 1
    elif(y[i] == 3):
        three = three + 1
    elif(y[i] == 4):
        four = four + 1
    elif(y[i] == 5):
        five = five + 1
    elif(y[i] == 6):
        six = six + 1
    if(y1[i] == 1):
        one1 = one1 + 1
    elif(y1[i] == 2):
        two1 = two1 + 1
    elif(y1[i] == 3):
        three1 = three1 + 1
    elif(y1[i] == 4):
        four1 = four1 + 1
    elif(y1[i] == 5):
        five1 = five1 + 1
    elif(y1[i] == 6):
        six1 = six1 + 1

pt.plot(x, y, 'y', 'o')
pt.plot(x, y, 'g', 'o')

pt.xlabel("Numbers")
pt.ylabel("Occurance")
pt.title("Graph Members Vs. Occurance")
pt.show()
