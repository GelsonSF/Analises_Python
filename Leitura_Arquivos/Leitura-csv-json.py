import pandas as pd
import json

arq_csv = pd.read_csv('C:\\nome da pasta\\nome do local dos arquivos csv\\arquivos\\arquivo_csv.csv', sep=';')

display(arq_csv)

with open('C:\\nome da pasta\\nome do local dos arquivos csv\\arquivos\\arquivo_csv\\arquivo_json.json') as list_player:
    dados = json.load(list_player)

df = pd.json_normalize(dados, "user")

display(df)
