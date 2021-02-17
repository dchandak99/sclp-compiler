import pandas as pd

df = pd.read_csv('data_into_5/base.csv')

df = df.rename(columns={"Race and ethnicity (combined)": "Race"})

df.shape

c = 0
for i in range(5):
    c = c + (i+1)*100000

df1 = df[:5000]
df2 = df[5000: 12000]
df3 = df[12000: 21000]
df4 = df[21000: 32000]
df5 = df[-13000:]

df[-1:]

df5.columns

df1.to_csv('data_for_e/base6.csv', index = False)
df2.to_csv('data_for_e/base7.csv', index = False)
df3.to_csv('data_for_e/base8.csv', index = False)
df4.to_csv('data_for_e/base9.csv', index = False)
df5.to_csv('data_for_e/base10.csv', index = False)






