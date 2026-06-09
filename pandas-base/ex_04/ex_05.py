# 04.05 - Selecione a primeira transação diária de cada cliente.

# %%

import pandas as pd

df = pd.read_csv("../../dados/transacoes.csv", sep=';')
df.head()

# %%

df['datetime'] = pd.to_datetime(df["DtCriacao"])
df['date'] = df['datetime'].dt.date

df_sort = df.sort_values(by=["IdCliente", "datetime"])
df_deduplicado = df_sort.drop_duplicates(subset=["IdCliente", "date"], keep="first")

df_deduplicado