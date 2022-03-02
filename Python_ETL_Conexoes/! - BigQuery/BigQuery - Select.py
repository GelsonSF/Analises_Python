get_ipython().system('pip install google-cloud-bigquery')

import os

from google.cloud.bigquery.client import Client


def credentials_bq():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\learn\\4 - Outros\\Chaves\\bqsql-339211-dd826cade8aa.json'

    bq_client = Client()


def consult_bq():
    consultaSQL = '''SELECT 
                        ano,
                        sigla_uf,
                        rede,
                        id_escola,
                        quantidade_matriculas
                    FROM 
                        `basedosdados.br_inep_censo_escolar.turma` 
                    LIMIT 100'''
    
    jobSQL = bq_client.query(consultaSQL)
    
    resultadoSQL = jobSQL.result()
    
    for linha in resultadoSQL:
        print('Ano:' + str(linha.ano) + 
              ', UF: '+ linha.sigla_uf + 
              ', Rede: ' + linha.rede + 
              ', Código da Escola: ' + str(linha.id_escola) + 
              ', Quantidade de Matriculas: ' + str(linha.quantidade_matriculas))


consult_bq()
