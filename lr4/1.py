import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def rand1(n):
    rand_list = []
    for i in range(n):
        rand_list.append(random.randint(3, 9))
    print(rand_list)


def rand2(n):
    res = random.sample(range(1, 50), n)
    print("Random number list is : " + str(res))


def rand3(n):
    res = [random.randrange(1, 50, 1) for i in range(n)]
    print("Random number list is : " + str(res))


def rand4(n):
    lis = []
    for _ in range(n):
        lis.append(random.randint(0, 51))
    print(lis)


def nprand1(n, m):
    print(list(np.random.randint(low=3, high=8, size=n)))
    print(list(np.random.randint(low=3, size=m)))


def nprand2(n, m):
    print(np.random.random_sample(size=n))
    print(np.random.random_sample(size=(n, m)))


def kubik(n: int) -> list:
    data = []
    while len(data) < n:
        data.append(random.randint(1, 6))
    return data


def count_rate(kub_data: list):
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kub_data.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate


def sort_rate(counted_rate: dict):
    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate


def create_dataframe(sorted_date: dict):
    df = pd.DataFrame(sorted_date, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
    return df


def probability_solving(dataframe: pd.DataFrame):
    sum_rate = dataframe['Частота'].sum()
    probability = []
    for i in dataframe['Частота']:
        probability.append(i / sum_rate)
    dataframe['Вероятность'] = probability
    return dataframe


def graphplot(df1, df2, df3, df4: pd.DataFrame):
    plt.subplot(2, 2, 1)
    plt.plot(df1['Количество выпаданий'], df1['Частота'], color='k')
    plt.plot(df1['Количество выпаданий'], df1['Частота'], 'ro')
    plt.grid()
    plt.title('100 бросков')
    plt.xlabel('Количество выпаданий')
    plt.ylabel('Частота')
    plt.subplot(2, 2, 2)
    plt.plot(df2['Количество выпаданий'], df2['Частота'], color='k')
    plt.plot(df2['Количество выпаданий'], df2['Частота'], 'ro')
    plt.grid()
    plt.title('1000 бросков')
    plt.xlabel('Количество выпаданий')
    plt.ylabel('Частота')
    plt.subplot(2, 2, 3)
    plt.plot(df3['Количество выпаданий'], df3['Частота'], color='k')
    plt.plot(df3['Количество выпаданий'], df3['Частота'], 'ro')
    plt.grid()
    plt.title('10000 бросков')
    plt.xlabel('Количество выпаданий')
    plt.ylabel('Частота')
    plt.subplot(2, 2, 4)
    plt.plot(df4['Количество выпаданий'], df4['Частота'], color='k')
    plt.plot(df4['Количество выпаданий'], df4['Частота'], 'ro')
    plt.grid()
    plt.title('1000000 бросков')
    plt.xlabel('Количество выпаданий')
    plt.ylabel('Частота')
    plt.show()


def graphbar(df1, df2, df3, df4: pd.DataFrame):
    plt.subplot(2, 2, 1)
    b1 = plt.bar(df1['Количество выпаданий'], df1['Частота'], color='r')
    plt.bar_label(b1, label_type='center', color='w')
    plt.title('100 бросков')
    plt.xlabel('Количество выпаданий')
    plt.ylabel('Частота')
    plt.subplot(2, 2, 2)
    b2 = plt.bar(df2['Количество выпаданий'], df2['Частота'], color='g')
    plt.bar_label(b2, label_type='center', color='w')
    plt.title('1000 бросков')
    plt.xlabel('Количество выпаданий')
    plt.ylabel('Частота')
    plt.subplot(2, 2, 3)
    b3 = plt.bar(df3['Количество выпаданий'], df3['Частота'], color='b')
    plt.bar_label(b3, label_type='center', color='w')
    plt.title('10000 бросков')
    plt.xlabel('Количество выпаданий')
    plt.ylabel('Частота')
    plt.subplot(2, 2, 4)
    b4 = plt.bar(df4['Количество выпаданий'], df4['Частота'], color='y')
    plt.bar_label(b4, label_type='center', color='w')
    plt.title('1000000 бросков')
    plt.xlabel('Количество выпаданий')
    plt.ylabel('Частота')
    plt.show()


df100 = pd.DataFrame(probability_solving(create_dataframe(sort_rate(count_rate(kubik(100))))))
df1k = pd.DataFrame(probability_solving(create_dataframe(sort_rate(count_rate(kubik(1000))))))
df10k = pd.DataFrame(probability_solving(create_dataframe(sort_rate(count_rate(kubik(10000))))))
df1mil = pd.DataFrame(probability_solving(create_dataframe(sort_rate(count_rate(kubik(1000000))))))
print(df100, df1k, df10k, df1mil, sep='\n')
graphplot(df100, df1k, df10k, df1mil)
graphbar(df100, df1k, df10k, df1mil)