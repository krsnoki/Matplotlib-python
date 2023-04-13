import matplotlib.pyplot as plt
import numpy as n
from numpy import random

x = random.choice(100, size = (10))
y = random.choice(100, size = (10))
y1 = random.choice(100, size = (10))

#giving differet colors to the scattergraph
'''

plt.scatter(x, y, color = 'blue')
plt.scatter(x, y1, color = 'yellow')
plt.show()
'''

#giving different colors to every dot
'''whwenever we have to show various regions and to show weightage of particular value
we have to use this type of size and colors'''
color = n.array(["red", "pink", "blue", "yellow", "cyan", "green", "orange", "black", "lemonchiffon", "gray"])
sizes = n.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

plt.scatter(x, y, color = 'blue')
plt.scatter(x, y1, c = color, s = sizes)
plt.show()
