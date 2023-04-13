#linear equation
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

s1 = [57, 86, 56, 96, 36, 45]
s2 = [65, 72, 92, 41, 20, 15]

slope, intercept, r, p, std_err = stats.linregress(s1, s2)
print(slope, end = " ")
print(intercept, end = " ")
print(r, end = " ")
print(p, end = " ")
print(std_err)

def ff(s1):
    return slope*s1 + intercept
plt.scatter(s1, s2)
model = list(map(ff, s1))
plt.plot(s1, model)
plt.show()
print(model)
