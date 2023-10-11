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

#Manipulando os dados da API e criando gráficos
pokemon_by_height = pokemon_df.sort_values(by='Height (m)', ascending=False).head()
print(pokemon_by_height)

fig, ax = plt.subplots()
height_barplot = ax.bar(pokemon_by_height['Name'], pokemon_by_height['Height (m)'], align='center')

for index, value in enumerate(pokemon_by_height['Height (m)']):
    ax.text(index, value + 0.1, str(value), horizontalalignment='center',verticalalignment='center')

for bar, typing in zip(height_barplot, pokemon_by_height['Type 1']):
    bar.set_color(type_colors[typing])

for bar, index, height in zip(range(0, 5), pokemon_by_height.index, pokemon_by_height['Height (m)']):
    pokemon_img = imread(
        f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{index + 1}.png', 
        format='png-pil'
        )
    
    img_position = [bar, height]
    ib = OffsetImage(pokemon_img, zoom=0.9)
    ib.image.axes = ax
    ab = AnnotationBbox(ib,
                    img_position,
                    frameon=False,
                    box_alignment=(0.5, 1.2)
                    )
    ax.add_artist(ab)
    

ax.set_title('Top 5 Pokemon by Height (Gen 1)')
ax.set_xlabel('Pokemon', labelpad=12.0)
ax.set_ylabel('Height (in meters)')
plt.tight_layout()
plt.show()