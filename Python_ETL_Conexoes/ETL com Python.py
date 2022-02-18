# Import de bibliotecas
import pandas as pd
import os
import pyodbc
import sqlalchemy

from sqlalchemy.engine import URL


# Criando a conexão com o banco de dados
try:
    driver='{SQL Server}'
    server='localhost\SQLEXPRESS'
    database='pyETL'
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


# Lendo arquivos na pasta
arq = "C:\\nome da pasta\\nome do local dos arquivos csv\\arquivos"

display(arq)


# Criando lista com os arquivos .csv e padronização da leitura do arquivo
list_arq = os.listdir(arq)

list_arq[:10]

list_df = []

for i in list_arq:
    arq_place = os.path.join(arq, i)
    df = pd.read_csv(arq_place, sep='|', encoding='latin-1')
    list_df.append(df)
df = pd.concat(list_df)

df[:1]


# Leitura dos arquivos compativeis com as tabelas a serem inseridas e tratamento de dados
tb_pessoa = df[["cod_pessoa", "genero", "data_nascimento"]].drop_duplicates()
display(tb_pessoa)


# Leitura dos arquivos compativeis com as tabelas a serem inseridas e tratamento de dados
tb_hobbie = df[["hobbies"]].drop_duplicates()
display(tb_hobbie)


# Leitura dos arquivos compativeis com as tabelas a serem inseridas e tratamento de dados
tb_clima = df[["clima"]].drop_duplicates()
display(tb_clima)


# Leitura dos arquivos compativeis com as tabelas a serem inseridas e tratamento de dados
tb_bebida = df[["bebida_favorita"]].drop_duplicates()
display(tb_bebida)


# Leitura dos arquivos compativeis com as tabelas a serem inseridas e tratamento de dados
tb_animal_est = df[["animal_estimacao"]].drop_duplicates()
display(tb_animal_est)


# Laço para criar o insert dos dados nas respectivas tabelas
for pessoas in tb_pessoa.itertuples():
    cod_pessoa = pessoas.cod_pessoa
    genero = pessoas.genero
    data_nascimento = pessoas.data_nascimento
    try:
        query = f"""
                    INSERT INTO PESSOA 
                        (COD_PESSOA, GENERO, DATA_NASCIMENTO)
                    VALUES
                        ('{cod_pessoa}', '{genero}', '{data_nascimento}') """
        cr.execute(query)
        cr.commit()
        
        print(f"Cadastro efetuado! Cod_pessoa= {cod_pessoa}")
    except Exception as e:
        print(f"{cod_pessoa} não foi possivel cadastrar! Pelo infortunio de {e}")


# Laço para criar o insert dos dados nas respectivas tabelas
for hobbies in tb_hobbie.itertuples():
    hobbie = hobbies.hobbies
    try:
        query = f"""
                    INSERT INTO HOBBIE
                        (TIPO_HOBBIE)
                    VALUES
                        ('{hobbie}')"""
        cr.execute(query)
        cr.commit()
        
        print(f"Cadastro Efetuado! Hobbie = {hobbie}")
    except Exception as e:
        print(f"{hobbie} não foi possivel cadastrar! Pelo infortunio de {e}")


# Laço para criar o insert dos dados nas respectivas tabelas
for climas in tb_clima.itertuples():
    clima = climas.clima
    try:
        query = f"""
                    INSERT INTO CLIMA
                        (TIPO_CLIMA)
                    VALUES
                        ('{clima}')"""
        cr.execute(query)
        cr.commit()
        
        print(f"Cadastro Efetuado! Clima = {clima}")
    except Exception as e:
        print(f"{clima} não foi possivel cadastrar! Pelo infortunio de {e}")


# Laço para criar o insert dos dados nas respectivas tabelas
for bebidas in tb_bebida.itertuples():
    bebida = bebidas.bebida_favorita
    try:
        query = f"""
                    INSERT INTO BEBIDA
                        (TIPO_BEBIDA)
                    VALUES
                        ('{bebida}')"""
        cr.execute(query)
        cr.commit()
        
        print(f"Cadastro Efetuado! Bebida = {bebida}")
    except Exception as e:
        print(f"{bebida} não foi possivel cadastrar! Pelo infortunio de {e}")
        
 
# Laço para criar o insert dos dados nas respectivas tabelas 
for animais in tb_animal_est.itertuples():
    animal = animais.animal_estimacao
    try:
        query = f"""
                    INSERT INTO ANIMAL_ESTIMACAO
                        (TIPO_ANIMAL)
                    VALUES
                        ('{animal}')"""
        cr.execute(query)
        cr.commit()
        
        print(f"Cadastro Efetuado! Animal = {animal}")
    except Exception as e:
        print(f"{animal} não foi possivel cadastrar! Pelo infortunio de {e}")
       

# Insert do grupo Pesquisa
try:
        df.to_sql('STG_PESQUISA', engine, index= False)
   
        query = f"""
                    INSERT INTO PESQUISA
                        (DATA_PESQUISA, COD_PESSOA, COD_ANIMAL_ESTIMACAO, COD_BEBIDA, COD_HOBBIE, COD_CLIMA)
                        (SELECT
                            STG.DATA_COLETA 	        AS 		DATA_PESQUISA			,
                            STG.COD_PESSOA 				AS		COD_PESSOA				,
                            AE.COD_ANIMAL_ESTIMACAO 	AS		COD_ANIMAL_ESTIMACAO 	,
                            BE.COD_BEBIDA  				AS		COD_BEBIDA 				,
                            HO.COD_HOBBIE 				AS		COD_HOBBIE 				,
                            CL.COD_CLIMA 				AS		COD_CLIMA
                        FROM
                            STG_PESQUISA            STG
                            JOIN ANIMAL_ESTIMACAO 	AE 	ON STG.ANIMAL_ESTIMACAO = AE.TIPO_ANIMAL
                            JOIN BEBIDA				BE 	ON BE.TIPO_BEBIDA = BEBIDA_FAVORITA
                            JOIN HOBBIE				HO 	ON STG.HOBBIES = HO.TIPO_HOBBIE
                            JOIN CLIMA				CL  ON STG.CLIMA = CL.TIPO_CLIMA);"""
        cr.execute(query)
        cr.commit()

        print(f"Cadastro Efetuado!")
except Exception as e:
    print(f"Não foi possivel cadastrar! Pelo infortunio de {e}")
           
