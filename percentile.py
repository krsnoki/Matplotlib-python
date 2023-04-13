import numpy as np
from numpy import random as rd

#s1 = rd.randint(1, 5, size = (10))
s1 = [4,14, 45, 85, 96, 63, 56,23]

print(s1)
x = np.percentile(s1, 90)
print(x)

'''
start = 4
end = 23
(start + end)*percentile value/100

for 25%
(4 + 23)/4
= 27/ 4
= 13.25
'''
