import matplotlib.pyplot as plt
import pandas as pd
import numpy

df = pd.read_csv('123.csv', sep=';')
y = df.groupby('Скоростное ограничение')['Наименование улицы'].nunique().values
print(y)
x = df['Скоростное ограничение'].unique()
numpy.ndarray.sort(x)
print(x)
plt.bar(x, y, width = 5)
plt.title('Количество улиц с ограничением скорости движения')
plt.xlabel('Скоростное ограничение')
plt.ylabel('Количество улиц')
plt.show()