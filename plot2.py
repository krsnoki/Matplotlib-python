from numpy import random as rd
import numpy as np
from matplotlib import pyplot as pt

x = rd.randint(10,12, size = (10))
y = rd.randint(50, size = (10))
y1 = rd.randint(50, size = (10))
pt.plot(x, y, 'y')
pt.plot(x, y1, 'g')

pt.xlabel("Numbers")
pt.ylabel("Occurance")
pt.title("Graph Members Vs. Occurance")
pt.show()
