import pandas as pd 

df = pd.read_csv('covid.csv', low_memory = False)

df1 = df.dropna()

df1.to_csv('base.csv', index = False)