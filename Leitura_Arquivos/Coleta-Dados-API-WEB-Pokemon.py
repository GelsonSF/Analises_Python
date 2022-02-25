import pandas as pd
import requests

infos = {}

def extract_pokemons_name():
    for i in range(1, 11):
        api_r = f'https://pokeapi.co/api/v2/pokemon/{i}/'
        resp = requests.get(api_r)
        requ = resp.json()

        for i in requ['forms']:
            for j in requ['types']:
                infos[i['name']] = j['type']['name']

        df = pd.DataFrame([infos])
        df = df.set_index(i['name'])
        df = df.T

    display(df)
	
def main():
	extract_pokemons_name()

main()
