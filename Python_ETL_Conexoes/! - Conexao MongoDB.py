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
