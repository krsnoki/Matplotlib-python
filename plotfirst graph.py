import matplotlib.pyplot as plt
import numpy as np
xpo = np.array([1,2,3,4, 5, 6, 7, 8, 9])

ypo = np.array([12, 23, 2, 15, 10, 45, 19, 5, 32])

y1 = np.array([12, 15, 16, 11, 10, 9, 14, 5, 12])
#color of line:
plt.plot(xpo, ypo, 'y')
plt.plot(xpo, y1, 'g')
plt.xlabel("Numbers")
plt.ylabel("Occurance")
#title:
plt.title("Graph Members Vs. Occurance")


plt.show()
