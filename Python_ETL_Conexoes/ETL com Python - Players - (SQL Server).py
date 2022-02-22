import pandas as pd
import os
import pyodbc
import sqlalchemy

from sqlalchemy.engine import URL

try:
    driver='{SQL Server}'
    server='localhost\SQLEXPRESS'
    database='dsf_pyETL'
    trusted_connection='yes'
    
    connection_string = f'DRIVER={driver};SERVER={server};'
    connection_string += f'DATABASE={database};'
    connection_string += f'TRUSTED_CONNECTION={trusted_connection}'
    
    connection_url = URL.create(
    "mssql+pyodbc", query={"odbc_connect": connection_string})
    
    engine = sqlalchemy.create_engine(connection_url)
    
    cnxn = pyodbc.connect(connection_string)
    cr = cnxn.cursor()
    
    print("Conexão realizada com sucesso!")
except Exception as e:
    print(f"Conexão não realizada! {e}")
	
df_arq = pd.read_csv("C:\\nome da pasta\\nome do local dos arquivos csv\\arquivos\\jogadores_csv.csv", sep=";")

display(df_arq)

df_arq.isnull().sum()

df_arq.dropna(axis=0, how='any', inplace=True)

tb_jogo = df_arq[["jogo"]].drop_duplicates()

display(tb_jogo)

tb_pais = df_arq[["pais"]].drop_duplicates()

display(tb_pais)

for jogos in tb_jogo.itertuples():
    jogo = jogos.jogo
    try:
        query = f"""
                    INSERT INTO JOGOS
                        (NOME_JOGO)
                    VALUES
                        ('{jogo}')"""
        cr.execute(query)
        cr.commit()
        
        print(f"{jogo} cadastrado com sucesso!")
    except Exception as e:
        print(f"Não foi possivel cadastrar, pelo infortunio de {e}")
		
for paises in tb_pais.itertuples():
    pais = paises.pais
    try:
        query = f"""
                    INSERT INTO PAIS
                        (NOME_PAIS)
                    VALUES
                        ('{pais}')"""
        cr.execute(query)
        cr.commit()
        
        print(f"{pais} cadastrado com sucesso!")
    except Exception as e:
        print(f"Não foi possivel cadastrar, pelo infortunio de {e}")
		
try:
        df_arq.to_sql('STG_JOGADOR', engine, index= False)
   
        query = f"""
                    INSERT INTO JOGADOR
                        (NOME_JOGADOR, GENERO, DATA_NASCIMENTO, NUM_VITORIAS, NUM_DERROTAS, TOTAL_PARTIDAS, COD_PAIS, COD_JOGO)
                        (SELECT
                            STG.JOGADOR		      AS		"NOME_JOGADOR"		,
                            STG.GENERO				  AS		"GENERO"			    ,
                            STG.DATA_NASCIMENTO	AS		"DATA_NASCIMENTO"	,
                            STG.NUM_VITORIAS		AS		"NUM_VITORIAS"		,
                            STG.NUM_DERROTAS		AS		"NUM_DERROTAS"		,
                            STG.TOTAL_PARTIDAS	AS		"TOTAL_PARTIDAS"	,
                            P.COD_PAIS				  AS		"COD_PAIS"			  ,
                            J.COD_JOGO				  AS		"COD_JOGO"			
                        FROM
                            STG_JOGADOR			STG
                            JOIN PAIS 			P	ON P.NOME_PAIS = STG.PAIS 
                            JOIN JOGOS			J	ON J.NOME_JOGO = STG.JOGO);"""
        cr.execute(query)
        cr.commit()

        print(f"Cadastro Efetuado!")
except Exception as e:
    print(f"Não foi possivel cadastrar! Pelo infortunio de {e}")
    
