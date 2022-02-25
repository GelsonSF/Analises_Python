import pandas as pd
import sqlalchemy
import datetime
import requests
import random
import pyodbc
import time

from sqlalchemy.engine import URL
from bs4 import BeautifulSoup

try:
    driver='{SQL Server}'
    server='localhost\SQLEXPRESS'
    database='coleta'
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
    
CRIAR_TABELA = '''
                    CREATE TABLE prod_coletado(
                        nome_produto VARCHAR(1000) NOT NULL,
                        valor_atual FLOAT NULL,
                        valor_procurado FLOAT NULL,
                        url VARCHAR(1000) NOT NULL,
                        data_coleta datetime2 
                    )'''

cr.execute(CRIAR_TABELA)
cr.commit()

def comportamento_humano(segundos=None):
    
    if not segundos:
        segundos = random.randrange(2,8)
    time.sleep(segundos)
    
def verifica_preco(produto, valor_procurado, valor_atual, url):
    
    if valor_atual < valor_procurado:
        print(f'Oportunidade de compra! O produto: {produto} abaixou o preço! R${valor_atual}\n Acesse: {url}')
    else:
        print(f'O produto {produto} não está com o valor desejado!')
        
def inserir_registro(produto, valor_atual, valor_procurado, URL):
   
    data_coleta = datetime.datetime.now()
    try:
        query = f"""
                    INSERT INTO PROD_COLETADO
                    (NOME_PRODUTO, VALOR_ATUAL, VALOR_PROCURADO,  URL, DATA_COLETA)
                    VALUES
                    ('{produto}', '{valor_atual}', '{valor_procurado}', '{URL}', '{data_coleta.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}')"""
        cr.execute(query)
        cr.commit()
        
        print(f'Registro inserido com sucesso: {produto}')
    except Exception as e:
        print(f'Não foi possível adicional o item {produto}. Erro: {e}')
        
lista_produtos = []

lista_produtos.append(('https://www.mercadolivre.com.br/notebook-acer-aspire-5-a514-53-prata-14-intel-core-i5-1035g1-4gb-de-ram-256gb-ssd-intel-uhd-graphics-g1-60-hz-1366x768px-windows-10-home/p/MLB18620959#reco_item_pos=1&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=f887ef83-09eb-4ab6-9f8e-90cc24a60a15&c_id=/home/navigation-recommendations/element&c_element_order=2&c_uid=652e5a3d-7333-4576-8ded-dca97f04af8d', 5000))
lista_produtos.append(('https://www.mercadolivre.com.br/notebook-lenovo-ideapad-15iml05-platinum-gray-156-intel-core-i5-10210u-8gb-de-ram-256gb-ssd-intel-uhd-graphics-620-1366x768px-windows-10-home/p/MLB18448291#reco_item_pos=3&reco_backend=machinalis-homes-pdp-boos&reco_backend_type=function&reco_client=home_navigation-recommendations&reco_id=f17a0262-5e38-40e8-a11c-be9d8aa7a221&c_id=/home/navigation-recommendations/element&c_element_order=4&c_uid=cf314d2a-106e-44a7-8df7-37778cc19c62', 1500))
lista_produtos.append(('https://www.mercadolivre.com.br/cafeteira-mondial-espresso-coffee-cream-premium-c-08-automatica-preta-e-prateada-expresso-120v/p/MLB14236778?pdp_filters=category:MLB9188#searchVariation=MLB14236778&position=3&search_layout=stack&type=product&tracking_id=c7efd754-fed9-45f9-be0b-fcd0852e78c7', 510))
lista_produtos.append(('https://www.mercadolivre.com.br/maquina-de-lavar-automatica-consul-cwh12-branca-12kg-127v/p/MLB14687693#searchVariation=MLB14687693&position=4&search_layout=stack&type=product&tracking_id=9e4ac379-fac9-400f-b7f9-1e721076a3b9', 2400))
lista_produtos.append(('https://www.mercadolivre.com.br/smart-tv-lg-ai-thinq-43lm631c0sb-led-full-hd-43-100v240v/p/MLB15186493?pdp_filters=category:MLB1002#searchVariation=MLB15186493&position=1&search_layout=grid&type=product&tracking_id=7fd48614-8a9d-4302-9878-1ce2dfbbfb9d', 1900))
lista_produtos.append(('https://www.mercadolivre.com.br/geladeira-auto-defrost-continental-tc41-branca-com-freezer-370l-127v/p/MLB15956843?pdp_filters=category:MLB181294#searchVariation=MLB15956843&position=1&search_layout=stack&type=product&tracking_id=0aff7058-322e-4603-b784-1f0113fafeae', 450))
lista_produtos.append(('https://www.mercadolivre.com.br/cama-box-gazin-flora-casal-de-188mx138m-marrom/p/MLB12206960?pdp_filters=category:MLB1574#searchVariation=MLB12206960&position=1&search_layout=grid&type=product&tracking_id=cbbdc31a-5537-49a2-8202-41e10db651cc', 1500))

for prod in lista_produtos:
    URL = prod[0]
    print('Aguardando comportamento humano...')
    comportamento_humano(random.randint(2,5))
    
    site = requests.get(URL)
    valor_procurado = prod[1]
    
    soup = BeautifulSoup(site.content, 'html.parser')
    produto = soup.find('h1', class_="ui-pdp-title").get_text()
    
    preco = soup.find('span', class_="andes-money-amount__fraction").get_text()
    valor_atual = float(preco.replace('.', ''))
    
    verifica_preco(produto, valor_procurado, valor_atual, URL)
    
    inserir_registro(produto, valor_atual, valor_procurado, URL)
    
print('Coleta finalizada com sucesso!')
