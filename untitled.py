import pandas as pd

arq = pd.read_csv('./data/dados.csv', sep=';', engine='python', encoding='utf-8');
print(arq)

print(arq.iloc[:3])
arq.iloc[20:]

arqCopy = arq.copy()
print(arqCopy)

arqCopy[arqCopy.isna().any(axis=1)]
arqCopy['Calories'] = arqCopy['Calories'].fillna(0)

data = arqCopy['Date'].fillna('1900/01/01')
arqCopy['Date'] = data

arqCopy['Date'] = pd.to_datetime(arqCopy['Date'], format='mixed')
arqCopy.info()

print(arqCopy)