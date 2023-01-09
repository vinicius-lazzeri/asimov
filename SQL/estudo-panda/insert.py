import pandas as pd

df1 = pd.read_csv("exemplo.csv", sep=",", decimal=".")
df1


#Para exportar um arquivo para outras formas.
df1.to_csv("exemplo2.csv", sep=";", decimal=",")