import pandas as pd
import datetime

numero_de_dias = 100

datas = pd.date_range(start='1/1/2021', periods=numero_de_dias)

datas.info

df = pd.DataFrame(range(numero_de_dias), columns=['number'], index=datas)
df

df.index

df.index[0]
df.index[0].day
df.index[0].month
df.index[0].year
df.index[0].hour

df[df.index.month == 1]

df[df.index.day == 10]

df['Month'] = df.index.month
df

df[df.index > datetime.datetime(2021, 1, 10)]
df