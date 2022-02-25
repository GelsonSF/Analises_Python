import pandas as pd
import requests

pokemons = []
    
def extract_pokemons_name():
    for i in range(1, 30):
        api_r = f'https://pokeapi.co/api/v2/pokemon/{i}/'
        resp = requests.get(api_r)
        requ = resp.json()
        
        for i in requ['forms']:
            pokemons.append(i['name'])
        for i in requ['types']:
            pokemons.append(i['type']['name'])
            
    df = pd.DataFrame(pokemons)
    display(df)
	
def main():
    extract_pokemons_name()
	
main()
