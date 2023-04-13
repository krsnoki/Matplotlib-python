
import matplotlib.pyplot as plt
import numpy as n
from numpy import random

x = random.randint(1, 100, size = (250))
#y = random.randint(1, 10, size = (250))
plt.hist(x)
plt.show()


#normal distribution histogram

x = n.random.normal(170, 10, 250)
plt.hist(x)
plt.show()
