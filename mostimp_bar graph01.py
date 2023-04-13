

'''bar graph'''
import matplotlib.pyplot as plt
import numpy as n
from numpy import random as r


x = n.array(["1990", "1995", "2000", "2005"])
sal = n.array([20000, 30000, 15000, 30000])

#for vertical bars
plt.bar(x, sal, color = "LemonChiffon",width = 0.4)
plt.show()

# for getting horizontal bars
plt.barh(x, sal, color = "Lightgreen", height = 0.2)
plt.show()
col = n.array(["red", "pink", "blue", "yellow", "cyan", "green", "orange", "black", "lemonchiffon", "gray"])
#bars having different colors
for i in range(0, 4):
    plt.bar(x[i], sal[i], color = col[i],width = 0.4)    
plt.show()
