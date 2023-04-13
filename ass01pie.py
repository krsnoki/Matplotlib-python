'''
take 100 values from 1 to 50 randomly
plot graph
for people 10 to 20
20 to 30
30 to 40
40 to 50
'''
import matplotlib.pyplot as plt
import numpy as n
from numpy import random as r

p = r.randint(1, 50, size = (100))

l = [0, 0, 0, 0]

for i in range(100):
    if(p[i] < 21):
        l[0] = l[0] + 1
    if(p[i] > 20 and p[i] < 31):
        l[1] = l[1] + 1
    if(p[i] > 30 and p[i] < 41):
        l[2] = l[2] + 1
    if(p[i] > 40 and p[i] < 51):
        l[3] = l[3] + 1
values = [0.1, 0.1, 0.1, 0.1]
color = n.array(["red", "pink", "blue", "yellow"])
lab = ["1 to 20","21 to 30", "31 to 40", "41 to 50"]
plt.pie(l, labels = lab, colors = color, explode = values, shadow = 4)
plt.title("Vaccination Rate")
plt.legend(title = "Age Groups")

plt.show()
