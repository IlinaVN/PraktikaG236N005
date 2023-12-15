import matplotlib.pyplot as plt
import pandas as pd
import numpy

df = pd.read_csv('123.csv', sep=';')
y = df.groupby('Административный округ')['Скоростное ограничение'].nunique().values
print(y)
x = df['Административный округ'].unique()
numpy.ndarray.sort(x)
print(x)
plt.barh(x, y)
plt.title('Количество улиц с ограничением скорости движения по АО')
plt.ylabel('АО')
plt.xlabel('Количество улиц')
plt.show()