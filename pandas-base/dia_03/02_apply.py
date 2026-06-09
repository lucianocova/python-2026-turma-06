# %%

import pandas as pd

df = pd.read_csv("../../dados/clientes.csv", sep=";")
df.head()

# %%

df["qtdePontos"].describe()

# <= 50 ->            Pouco
# 50 < x < 250 ->     Médio
# 250 =< x < 10000 -> Alto
# >= 10000 ->         Altíssimo

def classifica_pontos(pontos):
    if pontos <= 50:
        return "01-POUCO"
    
    elif 50 < pontos < 250:
        return "02-MÉDIO"
    
    elif 250 <= pontos < 10000:
        return "03-ALTO"
    
    elif pontos >= 10000:
        return "04-ALTÍSSIMO"

    else:
        return "05-DESCONHECIDO"

# %%

df["label_pontos"] = df["qtdePontos"].apply(classifica_pontos)
df["label_pontos"].value_counts().sort_index()

# %%

data = {
    "idCliente": "Téo",
    "flEmail": 0,
    "flTwitch": 1,
    "flYouTube": 0,
    "flBlueSky": 1,
    "flInstagram": 1,
    "qtdePontos": 2893712,
    "DtCriacao": "2026-01-01",
}

def nome_redes(row, sep=", "):
    redes = []
    if row["flTwitch"] == 1:
        redes.append("Twitch")
    if row["flYouTube"] == 1:
        redes.append("YouTube")
    if row["flBlueSky"] == 1:
        redes.append("BlueSky")
    if row["flInstagram"] == 1:
        redes.append("Instagram")
    return sep.join(redes)


# %%
df.apply(nome_redes, axis=1, sep=" | " )

# %%
df.apply(lambda row: nome_redes(row, " | "), axis=1)

# %%

df[['flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']].sum(axis=1)

# %%

df.apply(nome_redes, axis=1).apply(lambda x: "OURO" if len(x.split(",")) >= 2 else "PRATA")

# %%

idade = 10

maior_idade = "Sim" if idade >= 18 else "Não"
maior_idade

