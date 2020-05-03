import pandas as pd

pd.set_option('display.max_columns', 3)
df = pd.read_csv("./train.tsv", sep='\t')
colNames = ['Cena', 'Liczba pokoi', 'Metraż', 'Piętro', 'Lokalizacja', 'Opis']
df.columns = colNames

# 1)
dfMean = round(df['Cena'].mean())

with open("./out0.csv", 'w') as out0:
    out0.write(str(dfMean))

# 2)
df['Cena za m2'] = round(df['Cena'] / df['Metraż'] * 1000)
dfMeanSqm = round(df['Cena za m2'].mean())

dfOut1 = df[['Cena', 'Liczba pokoi', 'Cena za m2']].loc[(df['Liczba pokoi'] >= 3) & (df['Cena za m2'] < dfMeanSqm)]
dfOut1.to_csv('out1.csv', index=False, header=False)
