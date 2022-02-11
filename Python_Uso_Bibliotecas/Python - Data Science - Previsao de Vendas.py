import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

tabela = pd.read_csv('advertising.csv')
display(tabela)

sns.heatmap(tabela.corr(), cmap='Wistia', annot=True)

plt.show()

y = tabela['Vendas']
x = tabela[['TV', 'Radio', 'Jornal']]

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)

# Criar interligencia artificial (biblioteca pronta)
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# Treino da inteligencia Artificial
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

# Qual é o melhor modelo (determinar o melhor modelo para a aprendizagem)
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

from sklearn import metrics

print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))

# A arvore de decisão é o melhor modelo
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15,6))
sns.lineplot(data=tabela_auxiliar)
plt.show()

# Importar nova tabela com as informações de propaganda em TV, Radio e Jornal
# Passa a nova tabela para o predict do seu modelo
novos = pd.read_csv("novos.csv")
display(novos)

previsao = modelo_arvoredecisao.predict(novos)
print(previsao)



# Visualizar o melhor meio de propaganda
sns.barplot(x=x_treino.columns, y=modelo_arvoredecisao.feature_importances_)
plt.show()

