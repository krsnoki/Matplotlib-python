import numpy as np
from numpy import random as r
import matplotlib.pyplot as plt

age = [12, 52, 32, 26, 45, 78, 42]
m = np.mean(age)
print(m)
l1 = []
l2 = []
for i in range(len(age)):
    if(m > age[i]):
        l1.append(age[i])
    else:
        l2.append(age[i])
lab = ["Above", "Below"]
lp = [len(l1), len(l2)]
print("Ages Greator than Average:", )
print(l1)

print("Ages Lessor than Average:")
print(l2)

plt.pie(lp, labels = lab)
plt.title("Mean of ages")
plt.legend(title = "Parameters")
plt.show()

        
