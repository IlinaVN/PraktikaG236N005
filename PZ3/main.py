import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv', sep=',')
pvt = df[df.Survived==1].pivot_table(index=['PClass'], columns=['Sex'], values='Name', aggfunc='count')
data = pvt.loc[['1st', '2nd', '3rd'], ['male', 'female']]
data.plot.bar()
plt.xlabel('Класс')
plt.ylabel('Кол-во выживших')
plt.title("Количества выживших в классе по полу")
plt.show()
pvt = df[df.Survived==1].pivot_table(index=['Sex'], values='Age', aggfunc='mean')
data = pvt.loc[['male', 'female']]
data.plot.bar()
plt.xlabel('Пол')
plt.ylabel('Возраст')
plt.title("Средний возраст выживших")
plt.show()
