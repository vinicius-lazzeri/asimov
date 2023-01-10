import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df_data_gasolina_2000 = pd.read_csv('gasolina_2000+.csv', index_col=0)

df_data_gasolina_2010 = pd.read_csv('gasolina_2010+.csv', index_col=0)

df_data_gasolina_2000.to_sql('Gasolina 2000', conn, index_label='Gasolina 2000 Estatísticas')

df_data_gasolina_2010.to_sql('Gasolina 2010', conn, index_label='Gasolina 2010 Estatísticas')

df_gasolina_geral = pd.concat([df_data_gasolina_2000, df_data_gasolina_2010])

df_gasolina_geral.to_sql('Gráfico Geral', conn, index_label= 'Graf. Gasolina 2000 & 2010')

df_gasolina_geral.shape

df_gasolina_geral.info()
df_gasolina_geral.head()
df_gasolina_geral.tail()

df_gasolina_geral['DATA INICIAL'][3]
df_gasolina_geral['DATA INICIAL'] = pd.to_datetime(df_gasolina_geral['DATA INICIAL'])

df_gasolina_geral['DATA INICIAL']
df_gasolina_geral['DATA INICIAL'][3]

df_gasolina_geral['DATA FINAL'] = pd.to_datetime(df_gasolina_geral['DATA FINAL'])
df_gasolina_geral['DATA FINAL']

#Dica: :.2f = casas decimais depois do inteiro | :02d casas decimais antes do inteiro
df_gasolina_geral['ANO-MES'] = df_gasolina_geral['DATA FINAL'].apply(lambda x: f'{x.year}') + df_gasolina_geral['DATA FINAL'].apply(lambda x: f' - {x.month:02d}')

df_gasolina_geral['ANO-MES']
#visualizando nome das colunas para poder filtrar e extrair o que é solicitado.
df_gasolina_geral.columns
#extraindo a informação da coluna solicitada e seus valores
df_gasolina_geral['PRODUTO'].value_counts()

#Filtrando o DF para obter dados apenas do produto GASOLINA COMUM e gravando-o em uma variável específica.
df_gasolina_comum = df_gasolina_geral[df_gasolina_geral['PRODUTO'] == 'GASOLINA COMUM']
#executando variável
df_gasolina_comum
#Preço médio de revenda da gasolina em agosto de 2008:
df_gasolina_comum[df_gasolina_comum['ANO-MES'] == '2008 - 08']['PREÇO MÉDIO REVENDA'].mean()

#Preço médio de revenda da gasolina em maio de 2014 em São Paulo

df_gasolina_comum[(df_gasolina_comum['ANO-MES'] == '2014 - 05') & (df_gasolina_comum['ESTADO'] == 'SAO PAULO')]['PREÇO MÉDIO REVENDA'].mean() 

#Quais estados a gasolina ultrapassou a barreira dos R$5.00 e quando isso aconteceu

df_gasolina_comum[df_gasolina_comum['PREÇO MÉDIO REVENDA'] > 5][['ESTADO', 'ANO-MES', 'PREÇO MÉDIO REVENDA']].head(20)

#PREÇO MÉDIO DA GASOLINA EM 2012 NA REGIÃO SUL
#criando um dataframe (como uma fórmula) auxiliar para extrair 'ano-mes'e 'data final' para tornar prático para outras aplicações.

df_aux = df_gasolina_comum[df_gasolina_comum['DATA FINAL'].apply(lambda x: x.year) == 2012]
#OBTENDO O PREÇO MÉDIO DA GASOLINA EM 2012 NA REGIÃO SUL
df_aux[df_aux['REGIÃO'] == 'SUL']['PREÇO MÉDIO REVENDA'].mean()

#CRIANDO UMA TABELA CONTENDO A VARIAÇÃO PERCENTUAL AO ANO DO ESTADO DO RIO

df_gasolina_comum['MES'] = df_gasolina_comum['DATA FINAL'].apply(lambda x: x.month)
df_rio_de_janeiro = df_gasolina_comum[df_gasolina_comum['ESTADO'] == 'RIO DE JANEIRO']
df_mensal_rio = df_rio_de_janeiro.groupby('ANO-MES')[['PREÇO MÉDIO REVENDA', 'MES']].last()
#UTILIZANDO O MÊS DE DEZEMBRO DE CADA ANO PARA OBTER UMA MÉDIA DO ANO E COMPARA-LO AO DO ANO ANTERIOR DO MESMO MÊS

#MÉTODO SHIFT: ÚTIL PARA MERCADO FINANCEIRO E SERIES TEMPORAIS, FAZENDO UM DESLOCAMENTO DO CONJUNTO DE DADOS MANTENDO O ÍNDICE FIXO
(df_mensal_rio[df_mensal_rio['MES'] == 12] / df_mensal_rio[df_mensal_rio['MES'] == 12].shift(1)-1) * 100