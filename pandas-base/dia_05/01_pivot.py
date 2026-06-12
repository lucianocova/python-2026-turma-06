# %%

import pandas as pd

transacoes = pd.read_csv("../../dados/transacoes.csv",sep=';')
transacoes.head()

# %%

transacoes["Ano-Mes"] = pd.to_datetime(transacoes['DtCriacao']).dt.to_period("M")
transacoes.head()

# %%

groupby = transacoes.groupby(by=['Ano-Mes', 'DescSistemaOrigem'] )[["IdTransacao"]].count()
groupby = groupby.reset_index()

# %%

groupby.pivot_table(values="IdTransacao", index="Ano-Mes", columns="DescSistemaOrigem" )

# %%

analytics = transacoes.pivot_table(
    index="Ano-Mes",
    columns="DescSistemaOrigem",
    values="IdTransacao",
    aggfunc="count",
    fill_value=0
).reset_index()

import matplotlib.pyplot as plt

plt.plot(analytics["Ano-Mes"].dt.to_timestamp(), analytics["twitch"],'-o')
plt.plot(analytics["Ano-Mes"].dt.to_timestamp(), analytics["cursos"],'-o')
plt.legend(["Twitch", "Cursos"])
plt.xticks( rotation='vertical')
plt.grid()
plt.show()