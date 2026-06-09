# 04.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.

# %%

import pandas as pd

df = pd.read_csv( "../../dados/clientes.csv", sep=";")
df

# %%

redes = [
    "flTwitch",
    "flYouTube",
    "flBlueSky",
    "flInstagram",
]

# df["algum_rede"] = df[redes].sum(axis=1) >= 1
df["algum_rede"] = df[redes].any(axis=1).astype(int)
df