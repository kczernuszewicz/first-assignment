import pandas as pd


df = pd.read_csv("./train.tsv", sep='\t')
colNames = ['Cena z m2','Liczba pokoi', 'Metraż', 'Piętro','Lokalizacja','Opis']
df.columns = colNames
#
dfMean = round(df['Cena z m2'].mean())

with open("./out0.csv",'w') as out0:
    out0.write(str(dfMean))
