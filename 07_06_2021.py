import matplotlib.pyplot as plt
import numpy as np
from numpy import random

x = random.randint(1, 10, size = (100))

count = 0
cting = []
for i in range(1, 11):
    count = 0
    for j in range(1, 11):
        if(i == j):
            cting.append(count)
