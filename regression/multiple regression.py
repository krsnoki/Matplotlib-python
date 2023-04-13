import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

df = pd.read_excel("E:\marksavg.xlsx")
df = pd.DataFrame(df)
x = df[['Sem 1', 'Sem 2']]
y = df['Sem 3']

regr = linear_model.LinearRegression()
regr.fit(x, y)

predict = regr.predict([[67], [58]])
print(predict)
