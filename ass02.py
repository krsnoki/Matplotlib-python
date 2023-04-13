import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

l = []
print("Enter 10 elements: ")
for i in range(10):
    o = int(input(""))
    l.append(o)

mean = np.mean(l)
med = np.median(l)
mod = stats.mode(l)
x = np.array([10, 50, 60])
k = [mean, med, mod]

lab = ["Mean", "Median", "Mode"]
plt.bar(x, k)
plt.show()
