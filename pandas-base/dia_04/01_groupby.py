# %%

import pandas as pd

df = pd.read_csv("../../dados/transacoes.csv", sep=";")
df.head()

# %%

df.groupby(by="DescSistemaOrigem")[["IdTransacao"]].count()

# %%

df["ano"] = pd.to_datetime(df["DtCriacao"]).dt.year
df.head()

# %%

(df.groupby(by=["ano", "DescSistemaOrigem"], as_index=False)[["IdTransacao"]]
   .count())

# %%

df_report = (df.groupby(by=["ano", "DescSistemaOrigem"], as_index=False)
               .agg({"IdTransacao": "count", "QtdePontos": ["sum", "mean"] }))

df_report

# %%

df_report.columns

# %%

c1 = ("ano", "")
c2 = ("QtdePontos", "mean")

df_report[[c1, c2]] 

# %%

df_report.columns = ["ano", "origem", "qtdeTransacao", "TotalPontos", "mediaPontos"]
df_report

# %%

import numpy as np

(
    df.groupby(by=["ano", "DescSistemaOrigem"], as_index=False)
      .agg(somaPontos = ("QtdePontos", np.sum),
           mediaPontos = ("QtdePontos", np.mean),
           qtdeTransacoes=("IdTransacao", np.count_nonzero)
        )
)

# %%

def fodase(vetor_valores):
    return vetor_valores.quantile(0.99)


(df.groupby(by=["ano", "DescSistemaOrigem"], as_index=False)
   .agg({"QtdePontos": fodase}))

# %%

df.groupby(by=["ano", "DescSistemaOrigem"], as_index=False)[['QtdePontos']].describe()
