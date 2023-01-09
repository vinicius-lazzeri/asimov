import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': [1,2,np.nan],
    'B': [5,np.nan,np.nan],
    'C': [1,2,3]
})
df
df.dropna(axis=1, thresh=2)
df.fillna('Valor nulo')

df['A'].mean()

df['A'].fillna(value=df['A'].mean())

df.ffill()

