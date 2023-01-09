import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df_data_gasolina_2000 = pd.read_csv('gasolina_2000+.csv', index_col=0)

df_data_gasolina_2010 = pd.read_csv('gasolina_2010+.csv', index_col=0)

df_data_gasolina_2000.to_sql('Gasolina 2000', conn, index_label='Gasolina 2000 Estatísticas')

df_data_gasolina_2010.to_sql('Gasolina 2010', conn, index_label='Gasolina 2010 Estatísticas')

df_data_gasolina_geral = df_data_gasolina_2000 + df_data_gasolina_2010

