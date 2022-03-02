import os

from google.cloud.bigquery.client import Client
from google.cloud import bigquery

def credentials_bq():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\learn\\4 - Outros\\Chaves\\bqsql-339211-dd826cade8aa.json'

bq_client = Client(project="bqsql-339211")

def create_schema_bq():
    schema = [
        bigquery.SchemaField("cod","INTEGER"),
        bigquery.SchemaField("descritor","STRING"),
        bigquery.SchemaField("data","DATE"),
        bigquery.SchemaField("casado","BOOLEAN"),
    ]
    
    table_id = "bqsql-339211.apenas_um_teste.cliente_python1"
    
    table = bigquery.Table(table_id, schema)

    table = bq_client.create_table(table)

    print(f"Tablea Criada {table.project}.{table.dataset_id}.{table.table_id}")
    
create_schema_bq()
