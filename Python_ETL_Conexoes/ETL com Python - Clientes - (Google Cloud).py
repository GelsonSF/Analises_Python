import os

from google.cloud.bigquery.client import Client
from google.cloud import bigquery

def credentials_bq():
    global bq_client
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Local-Arquivo\\Arquivos.json'   
    
    bq_client = Client(project="nome-projeto")
	
def create_schema_bq(schema, table_id):
    credentials_bq()
    
    global table
    
    table = bigquery.Table(table_id, schema)
    table = bq_client.create_table(table)

    print(f"Tabela Criada {table.project}.{table.dataset_id}.{table.table_id}")
	
def load_schema_bq(uri):
    job_config = bigquery.LoadJobConfig(schema=schema, skip_leading_rows=1, source_format=bigquery.SourceFormat.CSV)

    load_job = bq_client.load_table_from_uri(source_uris=uri, destination=table_id, job_config=job_config)
    load_job.result()

    print(f"Tabela Carregada {table_id}")
	
schema = [
        bigquery.SchemaField("cod_agencia","STRING"),
        bigquery.SchemaField("nome_agencia","STRING")
    ]
    
table_id = "local-dos-dados.Id.agencias"

create_schema_bq(schema, table_id)

uri = 'gs://local-dos-dados/externo/arquivo.csv'

load_schema_bq(uri)

schema = [
        bigquery.SchemaField("cpf","STRING"),
        bigquery.SchemaField("nome_cliente","STRING")
    ]
    
table_id = "bqsql-339211.ByteBank.clientes"

create_schema_bq(schema, table_id)

uri = 'gs://bqsql-339211/externo/Clientes.csv'

load_schema_bq(uri)

schema = [
        bigquery.SchemaField("cod_conta","STRING"),
        bigquery.SchemaField("cod_agencia","STRING"),
        bigquery.SchemaField("cpf","STRING"),
        bigquery.SchemaField("tipo_conta","INTEGER")
    ]
    
table_id = "bqsql-339211.ByteBank.contas"

create_schema_bq(schema, table_id)

uri = 'gs://bqsql-339211/externo/LocalCliente.csv'

load_schema_bq(uri)
