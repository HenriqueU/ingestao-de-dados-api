from ingestão_de_dados_com_api import pokemon_df, type_colors
from matplotlib import pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from imageio.v2 import imread

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