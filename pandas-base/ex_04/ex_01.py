# 04.01 - Crie uma coluna nova “twitch_points” que é resultado da multiplicação do saldo de pontos e a marcação da twitch
# %%
import pandas as pd

df = pd.read_csv("../../dados/clientes.csv", sep=";")
df

# %%

df['twitch_points'] = df["qtdePontos"] * df['flTwitch']
df.head()