import pandas as pd
import plotly.express as px

tabela = pd.read_csv('telecom_users.csv')

display(tabela)

tabela = tabela.drop('Unnamed: 0', axis=1)

display(tabela.info())
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')
display(tabela.info())

tabela = tabela.dropna(how='all', axis=1)
tabela = tabela.dropna(how='any', axis=0)

print(tabela['Churn'].value_counts())
print(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format))

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()