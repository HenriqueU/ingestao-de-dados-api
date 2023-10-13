from ingestão_de_dados_com_api import pokemon_df, type_colors
import pandas as pd
from matplotlib import pyplot as plt

#Limpeza de Dados
types_by_qtd = pokemon_df[["Type 1", "Type 2"]].apply(pd.Series.value_counts)[1:]
types_by_qtd.fillna(0, inplace=True)
types_by_qtd['Total Qtd'] = types_by_qtd['Type 1'] + types_by_qtd['Type 2']
types_by_qtd = types_by_qtd.astype(int)
types_by_qtd.sort_values(by='Total Qtd', ascending=False, inplace=True)

#Criando gráficos
fig, ax = plt.subplots()

type_qtd_barhplot = ax.barh(types_by_qtd.index, types_by_qtd['Total Qtd'])

for index, value in enumerate(types_by_qtd['Total Qtd']):
    ax.text(value + 0.35, index, str(value), horizontalalignment='center',verticalalignment='center')

for bar, typing in zip(type_qtd_barhplot, types_by_qtd.index):
    bar.set_color(type_colors[typing])

ax.invert_yaxis()
ax.set_title("Pokemon Type Quantity (Gen 1)")
ax.set_xlabel("Type Quantity")
plt.tight_layout()
plt.show()