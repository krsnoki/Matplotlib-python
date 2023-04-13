import numpy as np
import matplotlib.pyplot as plt

age = [10, 20, 35, 30, 40, 45, 50, 41]
m = np.median(age)
l = np.sort(age)

for i in range(len(age)):
    if(m > age[i]):
        l1.append(age[i])
    else:
        l2.append(age[i])
print(l)
print(m)

print("Above Median:")
print(l1)
print("Below Median:")
print(l2)

el = [len(l1), len(l2)]
lab = ["Above median", "below average"]
c = ["pink", "violet"]

plt.pie(el, labels = lab, colors = c)
plt.title("Median count")
plt.show()
