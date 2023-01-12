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

#Tabela contendo uma série temporal com a diferença absoluta e percentual entre os valores mais baratos e caros, também apresentando todos os estados e seus devidos registros de gasolina mais barata e mais cara entre 2000 e 2020. 

#Criando uma variável para recolher as informações através de um groupby
df_max = df_gasolina_comum.groupby('ANO-MES').max()['PREÇO MÉDIO REVENDA']
df_min = df_gasolina_comum.groupby('ANO-MES').min()['PREÇO MÉDIO REVENDA']

#Recolhendo as informações através dos extremos máximos e mínimos por índices
idx_max = df_gasolina_comum.groupby('ANO-MES')['PREÇO MÉDIO REVENDA'].idxmax()
idx_min = df_gasolina_comum.groupby('ANO-MES')['PREÇO MÉDIO REVENDA'].idxmin()


#Criando um DF vazio para poder enriquece-lo com as informações
df_diff = pd.DataFrame()

#Colunas contendo as informações descritas nas variáveis

df_diff['DIFERENÇA ABSOLUTA'] = df_max - df_min

df_diff['DIFERENÇA PERCENTUAL'] = (df_max - df_min) / df_min * 100

df_diff['MAX'] = df_max
df_diff['MIN'] = df_min

#Para não dar erro de leitura da informação e prevenir de 'NaN', utilizando values e posicionando as informações de acordo com seus estados.
df_diff['ESTADO MÁX'] = df_gasolina_comum.loc[idx_max, :][['ESTADO']].values
df_diff['ESTADO MIN'] = df_gasolina_comum.loc[idx_min, :][['ESTADO']].values

#Estado com as maiores ocorrências de estado com a gasolina mais cara durante esses 20 anos.
df_diff['ESTADO MÁX'].value_counts()

#Estado com as menores ocorrências de estado com a gasolina mais cara durante esses 20 anos.
df_diff['ESTADO MIN'].value_counts()


