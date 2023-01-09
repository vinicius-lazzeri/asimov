import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4], 'col2':[444,555,666,444], 'col3':['abc', 'def', 'ghi', 'xyz']})
df.head()

df.info() #Retorna o tipo de dados de cada coluna de um data frame

df.memory_usage() #Retorna quantidade de memória utilizada por cada coluna

df

df['col2'].unique() #Retorna apenas valores únicos

df['col2'].nunique() #Retorna a quantidade de valores únicos

df['col2'].value_counts() #Retorna os valores únicos e suas quantidades em um data frame

df['col2'].value_counts().index

def comp(x):
    return x ** 2 + 3
df['col1'].apply(comp)

df['col1_calc'] = df['col1'].apply(comp)

df

#Pode utilizar lambda também, reduzindo os códigos acima para apenas uma linha:
df['col1'].apply(lambda x: x ** 2 + 3)

df['col1'].sum() #Somar os valores da coluna
df['col1'].mean() #Calcular média
df['col1'].product() #Calcular o produto dos valores
df['col1'].std() #Calcular o desvio padrão para estatística
df['col1'].max() #Exibir o maior valor
df['col1'].min() #Exibir o menor valor
df['col1'].idxmax() #Exibe qual index apresenta o valor máximo

#Realiza o somatório da coluna 1 sempre que a coluna 2 apresentar um certo valor (neste caso: 444)
df[df['col2'] == 444]
df[df['col2'] == 444]['col1'].sum()

#Para ordenar o dataframe através de uma coluna específica como referência
df.sort_values(by='col2')

data = {'A':['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B':['one', 'one', 'two', 'two', 'one', 'one'],
        'C':['x', 'y', 'x', 'y', 'x', 'y'],
        'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)

df

#Criando uma nova coluna 'E' de acordo com uma condição
#Função Map: pede uma orientação ao pandas para como tratar/ler seus dados, como 'one = 1 | two = 2'
dict_map = {'one': '1', 'two': '2'}
df['B'].map(dict_map)

df['E'] = df['B'].map(dict_map)

df

#pivot table: é uma forma que o pandas oferece para reorganizar os dados em função de alguma coisa

df.pivot_table(index='A', columns='B', values='D')