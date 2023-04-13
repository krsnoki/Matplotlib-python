import pandas as pd
import numpy as np
dict = {
    "Brand": "BMW",
    "Prize": 25000000,
    "Model": 2020,
    "Age": 12
    }

print(dict)
#If yoou want to

s1 = pd.Series(dict, index = ["Prize", "Model", "Age", "Brand"])
print(s1)
for i in range(1, len(dict)):
    print(s1[i])
