import pandas as pd


def kategoria(df, krepezh_dict, decor_dict):
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


def columns(df):
    df.insert(7, "Группа", 0)
    df.insert(8, "Категория", 0)
    df.insert(9, "Производитель", 0)


df1 = pd.read_excel("C:\PMiAOZD\PZ11\Машина 1.xlsx")
df2 = pd.read_excel("C:\PMiAOZD\PZ11\Машина 2.xlsx")
krepezh_dict = {"Болт", "Гайка", "Штифт", "Шайба", "Шуруп"}
decor_dict = {"Коврики", "Подушки"}
columns(df1)
columns(df2)
kategoria(df1, krepezh_dict, decor_dict)
kategoria(df2, krepezh_dict, decor_dict)
diff = pd.concat([df1,df2]).drop_duplicates(keep=False)
# diff.reset_index(inplace=True)
diff = diff.sort_values(['Наименование компоненты'])
print(diff)
df1.to_excel('Машина 1-Разметка.xlsx')
df2.to_excel('Машина 2-Разметка.xlsx')
diff.to_excel('Различие.xlsx')
