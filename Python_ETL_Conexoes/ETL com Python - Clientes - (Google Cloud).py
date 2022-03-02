import os

from google.cloud.bigquery.client import Client
from google.cloud import bigquery

def credentials_bq():
    global bq_client
    
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\learn\\4 - Outros\\Chaves\\bqsql-339211-dd826cade8aa.json'   
    
    bq_client = Client(project="bqsql-339211")

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

def read_schema_bq(query):
    job_sql = bq_client.query(query)
    
    resultado_sql = job_sql.result()
    
    for datasource in resultado_sql:
        print('Agência: ' + str(datasource.cod_agencia) + 
              ',\n Nome da Agência: '+ datasource.nome_agencia + 
              ',\n Conta: ' + datasource.cod_conta + 
              ',\n Cliente: ' + datasource.nome_cliente + 
              ',\n CPF: ' + datasource.cpf + 
              ',\n Código: ' + str(datasource.tipo_conta) + 
              ',\n Tipo da Conta: ' + datasource.tipo)

def delete_schema_bq(table_id):
    bq_client.delete_table(table_id, not_found_ok=True)
    
    print(f'Tabela {table_id} excluida com sucesso!')

schema = [
        bigquery.SchemaField("cod_agencia","STRING"),
        bigquery.SchemaField("nome_agencia","STRING")
    ]
    
table_id = "bqsql-339211.ByteBank.agencias"

create_schema_bq(schema, table_id)

uri = 'gs://bqsql-339211/externo/Agencias.csv'

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

uri = 'gs://bqsql-339211/externo/ContasCorrente.csv'

load_schema_bq(uri)

query = '''
            SELECT 
                AG.cod_agencia,
                AG.nome_agencia,
                C.cod_conta,
                CL.nome_cliente,
                CL.cpf,
                C.tipo_conta,
                CASE
                    WHEN C.tipo_conta = 1 THEN 'Conta Corrente'
                ELSE
                    'Conta Poupança'
                END AS tipo
            FROM 
                `bqsql-339211.ByteBank.contas`          C
                JOIN `bqsql-339211.ByteBank.clientes`   CL ON C.cpf = CL.cpf
                JOIN `bqsql-339211.ByteBank.agencias`   AG ON C.cod_agencia = AG.cod_agencia  '''

read_schema_bq(query)
