import pandas as pd
import numpy as np

df_obesidade = pd.read_csv('obesity_cleaned.csv')
df_obesidade['Obesity (%)'].value_counts()
df_obesidade['Obesity (%)'].iloc[0].split()
df_obesidade.columns
del df_obesidade['Unnamed: 0']
df_obesidade['Obesity'] = df_obesidade['Obesity (%)'].apply(lambda x: x.split()[0])
df_obesidade['Obesity']
df_obesidade.loc[df_obesidade['Obesity'] == 'No', 'Obesity'] = np.nan
df_obesidade['Obesity'] = df_obesidade['Obesity'].dropna()
df_obesidade['Obesity'] = df_obesidade['Obesity'].apply(lambda x: float(x))
df_obesidade['Year'] = df_obesidade['Year'].apply(lambda x: int(x))
df_obesidade.set_index('Year', inplace=True)

df_obesidade[df_obesidade.index == 2015].groupby('Sex').mean()

df_obesidade_start = df_obesidade[df_obesidade.index == 1975]
df_obesidade_end = df_obesidade[df_obesidade.index == 2016]

df_obesidade_start.set_index('Country', inplace=True)
df_obesidade_end.set_index('Country', inplace=True)
df_obesidade_ev = df_obesidade_end[df_obesidade_end['Sex'] == 'Both sexes']['Obesity'] - df_obesidade_start[df_obesidade_start['Sex'] == 'Both sexes']['Obesity']
df_obesidade_ev.sort_values().dropna().head(5)
df_obesidade_ev.sort_values().dropna().tail(5)

df_obesidade_end[df_obesidade_end.index == 'Tuvalu']

df_2015 = df_obesidade[df_obesidade.index == 2015]
df_2015[df_2015['Obesity'] == df_2015['Obesity'].max()]

df_brazil = df_obesidade[df_obesidade['Country'] == 'Brazil']
(df_brazil[df_brazil['Sex'] == 'Female']['Obesity'] - df_brazil[df_brazil['Sex'] == 'Male']['Obesity']).plot()

df_both = df_obesidade[df_obesidade['Sex'] == 'Both sexes']
df_both.groupby('Year')['Obesity'].mean().plot()