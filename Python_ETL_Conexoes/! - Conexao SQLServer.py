import pandas as pd
import os
import pyodbc
import sqlalchemy

from sqlalchemy.engine import URL

try:
    driver='{SQL Server}'
    server='localhost\SQLEXPRESS'
    database='nome_database'
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
    
