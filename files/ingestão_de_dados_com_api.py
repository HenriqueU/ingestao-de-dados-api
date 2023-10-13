#Site da PokeAPI: https://pokeapi.co/
#Documentação da PokeAPI: https://pokeapi.co/docs/v2

import requests
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from imageio.v2 import imread

#Coletando dados da API
pokemon_name = []
pokemon_type1 = []
pokemon_type2 = []
pokemon_height = []
pokemon_weight = []

for nat_dex_number in range(1, 152):
    pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nat_dex_number}").json()

    pokemon_name.append(pokemon['name'].capitalize())

    type_qtd = len(pokemon['types'])
    if type_qtd == 1:
        pokemon_type1.append(pokemon['types'][0]['type']['name'].capitalize())
        pokemon_type2.append('-')
    else:
        pokemon_type1.append(pokemon['types'][0]['type']['name'].capitalize())
        pokemon_type2.append(pokemon['types'][1]['type']['name'].capitalize())

    pokemon_height.append(pokemon['height'] / 10)
    pokemon_weight.append(pokemon['weight'] / 10)

#Armazenando os dados coletados em um DataFrame
pokemon_data = {
    "Name": pokemon_name,
    "Type 1": pokemon_type1,
    "Type 2": pokemon_type2,
    "Height (m)": pokemon_height,
    "Weight (Kg)": pokemon_weight
}

pokemon_df = pd.DataFrame(pokemon_data)
pokemon_df.describe()
pokemon_df.info()

#Cor em hexadecimal de cada tipo
type_colors = {
    "Normal": "#A8A77A",
    "Fire": "#EE8130",
    "Water": "#6390F0",
    "Electric": "#F7D02C",
    "Grass": "#7AC74C",
    "Ice": "#96D9D6",
    "Fighting": "#C22E28",
    "Poison":"#A33EA1",
    "Ground": "#E2BF65",
    "Flying": "#A98FF3",
    "Psychic": "#F95587",
    "Bug": "#A6B91A",
    "Rock": "#B6A136",
    "Ghost": "#735797",
    "Dragon": "#6F35FC",
    "Dark": "#705746",
    "Steel": "#B7B7CE",
    "Fairy": "#D685AD"
}