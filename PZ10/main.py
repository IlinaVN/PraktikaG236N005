import pandas as pd

df = pd.read_excel("E:\PMiAOZD\PZ10\Машина 1.xlsx")
df.insert(7, "Группа", 0)
df.insert(8, "Категория", 0)
df.insert(9, "Производитель", 0)
krepezh_dict = {"Болт", "Гайка", "Штифт", "Шайба", "Шуруп"}
decor_dict = {"Коврики", "Подушки"}
for i in range(len(df)):
    if i < 5:
        df["Группа"].loc[df.index[i]] = "Сборка"
    else:
        df["Группа"].loc[df.index[i]] = "Компонент"
    if df["Наименование компоненты"].loc[df.index[i]] in krepezh_dict:
        df["Категория"].loc[df.index[i]] = "Крепёж"
    elif df["Наименование компоненты"].loc[df.index[i]] in decor_dict:
        df["Категория"].loc[df.index[i]] = "Декор"
    elif df["Группа"].loc[df.index[i]] == "Сборка":
        df["Категория"].loc[df.index[i]] = "Сборка"
    else:
        df["Категория"].loc[df.index[i]] = "Детали"
    if "ГОСТ" in df['Код компоненты'].loc[df.index[i]]:
        df["Производитель"].loc[df.index[i]] = "РФ по ГОСТ"
    elif df["Код компоненты"].loc[df.index[i]].isascii():
        df["Производитель"].loc[df.index[i]] = "Иностранные"
    else:
        df["Производитель"].loc[df.index[i]] = "РФ"
df.to_excel('Машина 1-Разметка.xlsx')