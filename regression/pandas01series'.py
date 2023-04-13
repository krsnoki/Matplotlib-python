import pandas as pd
import numpy as np

data = np.array([2, 4, 5, 8, 12, 16, 14])
s = pd.Series(data, index = [])
d = np.array([10, 10, 10, 10,10, 10, 10 ])
s1 = pd.Series(d)

w = pd.Series(5)
w = s + s1
print(w)
