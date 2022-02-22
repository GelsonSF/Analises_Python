!pip install pymongo
!pip install dnspython

import pandas as pd
import pymongo
import json
import os

try:
    cnxn = "mongodb+srv://<usuario>:<senha>@mdblearn.c5xil.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    cr = MongoClient(cnxn) 
    db = cr.bd_chess
    collection = db.cl_chess    
    
    print(f"Tudo certo, conexão com banco realizada!")
except Exception as e:
    print(f"Ops, algo de errado não está certo, não foi possivel conectar! {e}")
	
with open("C:\\nome da pasta\\nome do local dos arquivos csv\\arquivos\\arquivo.json') as list_chess:
    dados = json.load(list_chess)

df = pd.json_normalize(dados, "user")
display(df)

chess_df = df.to_dict('records')

chess_df[:3]

try:
    for users in chess_df:
        user_id = collection.insert_one(users)
        user_id.inserted_id
        
    print(f"Cadastrado com sucesso!")
except Exception as e:
    print(f"Não foi possivel cadastar, pelo infortunio de: {e}")
