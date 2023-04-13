import pandas as pd
import numpy as np
s1 = pd.Series(5, index = ['a', 'b', 'c', 'd', 'e', 'f'])


s2 = pd.Series([1, 2, 3, 4, 5], index = ['a', 'b', 'c', 'd', 'e'])

print(s2[['c','a','d', 'b']])

'''
if we want to check if we pass zero will the series be accesible??
'''

print(s2[:3])
print(s2[-1])
