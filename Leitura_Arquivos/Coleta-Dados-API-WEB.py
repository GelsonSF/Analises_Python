import requests
import pandas as pd

#### Preparação para a extração dos nomes de pokemon ####

try:
    url_name = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1200'
    res_name = requests.get(url_name)
    res_name_json = res_name.json()

    print(f'Conexão com API realizada! {res_name}')
except Exception as e:
    print(f'Problema ao se conectar a API! {e}')

#### Extração dos nomes de pokemon, inclusão em uma lista e transformação em Dataframe. ####

try:
    pokemons = []
    
    def extract_pokemons_name():       
        for i in res_name_json['results']:
            pokemons.append(i['name'])
                
    extract_pokemons_name()
    
    pokemons_names = pd.DataFrame(pokemons, columns = ['Name']) 
    
    print(f'Extração realizada com sucesso!')
except Exception as e:
    print(f'Não foi possível realizar a extração! {e}')

#### Demostrativo da lista com os nomes dos pokemons ####

display(pokemons_names)

#### Criação de uma função para buscar informações dos pokemons, percorrendo uma lista. ####

def busca_pokemon(pokemons_names):
    try:
        api = f'https://pokeapi.co/api/v2/pokemon/{pokemons_names}'
        res = requests.get(api)
        if res.ok:
            return res.json()

        print(f'Conexão com API realizada! {res}')
    except Exception as e:
        print(f'Problema ao se conectar a API! {e}')

#### Teste da função busca_pokemon ####

busca_pokemon(pokemons_names['Name'][1])

#### Busca das informações dos 3 primeiros pokemons da lista, e load para  ####

try:
    info_pokemons = []

    for infos in pokemons_names['Name'][:3]:
        info = busca_pokemon(infos)
        print(f'{info}')
        info_pokemons.append(info),
    
    #df = pd.DataFrame(lista)
    df = pd.DataFrame(lista, columns = ['id', 'order' , 'name', 'forms', 'base_experience', 'abilities', 'moves', 'species', 'stats', 'types', 'height', 'weight', 'location_area_encounters', 'game_indices', 'sprites'])
        
    print(f'Lista populada com sucesso!')
except Exception as e:
    print(f'Problema ao buscar e popular a lista! {e}')

#### Teste do dataframe ####

display(df)
