import pandas as pd

pd.set_option('display.max_columns', None)
df1 = pd.read_csv("./train.tsv", sep='\t')
df2 = pd.read_csv("./description.csv")

colNames1 = ['Cena', 'Liczba pokoi', 'Metraż', 'Piętro', 'Lokalizacja', 'Opis']
colNames2 = ['Piętro', 'Nazwa piętra']
df1.columns = colNames1
df2.columns = colNames2

df3 = pd.merge(df1, df2, left_on='Piętro', right_on='Piętro', how='left')
df3.to_csv('out2.csv', index=False)
