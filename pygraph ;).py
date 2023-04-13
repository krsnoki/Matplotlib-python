import matplotlib.pyplot as plt
import numpy as n
from numpy import random
'''
y = n.array([45, 52, 65, 25,35, 96, 86])

plt.pie(y)
plt.show()'''

#giving proper labels to the pie graph
y = n.array([45, 52, 65, 25,35, 96, 86])
lab = ["Sunday", "Monday", "Tuesday", "wednesday", "Thursday", "Friday", "Saturday"]
values = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
color = n.array(["red", "pink", "blue", "yellow", "cyan", "green", "orange", "black", "lemonchiffon", "gray"])

plt.pie(y, labels = lab, explode = values, shadow = 15, colors = color)
plt.legend(loc = "best", title = "Days")
'''
locations:
        best
	upper right
	upper left
	lower left
	lower right
	right
	center left
	center right
	lower center
	upper center
	center
'''
plt.title("Work Done Each day of week")
plt.show()
