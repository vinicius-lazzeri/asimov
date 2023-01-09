import pandas as pd

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']},
    index=[0,1,2,3]
)

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']},
    index=[4,5,6,7]
)

df3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']},
    index=[8,9,10,11]
)

df1
df2
df3

#Concat encaixa um DF em outro. axis=1 concatena horizontalmente em caso de haver mais colunas em um df específico. Concat é ideal quando os DFs possuem os mesmos índices e colunas. Em caso de colunas a mais = axis=1 | índices a mais: axis=0.
pd.concat([df1,df2,df3], axis=1)

esquerda = pd.DataFrame({
    'Key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

direita = pd.DataFrame({
    'Key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

esquerda
direita


#O merge funciona nos auxiliando encaixando os dados que de alguma forma a utilizar as colunas como referência para como proceder com este encaixe. Onde 'key' neste caso é a referência.
pd.merge(esquerda, direita, on='Key')

esquerda = pd.DataFrame({
    'Key1': ['K0', 'K0', 'K1', 'K2'],
    'Key2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

direita = pd.DataFrame({
    'Key1': ['K0', 'K1', 'K1', 'K2'],
    'Key2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

esquerda
direita

pd.merge(esquerda, direita, on=['Key1', 'Key2'])

pd.merge(esquerda, direita, how='outer', on=['Key1', 'Key2'])