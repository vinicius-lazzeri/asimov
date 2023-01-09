import pandas as pd
#Criando um dataframe

data = {'Classe':['JR', 'JR', 'PLENO', 'PLENO', 'SENIOR', 'SENIOR'],
        'Nome': ['Jorge', 'Carlos', 'Roberta', 'Patrícia', 'Bruno', 'Ana'],
        'Venda': [200,120,340,124,243,350]

}

df = pd.DataFrame(data)
df
group = df.groupby('Classe')
group.sum()
group.mean()

df.groupby('Classe').sum()
df.groupby('Classe').min()
df.groupby('Classe').max()

df

df2 = df.copy()

df2['Venda'] = [150, 432, 190, 230, 410, 155]
df2

df3 = pd.concat([df, df2])
df3

df3.groupby(['Classe', 'Nome']).sum()
df3.groupby(['Classe', 'Nome']).max()