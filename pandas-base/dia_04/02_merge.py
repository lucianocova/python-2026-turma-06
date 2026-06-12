# %%

import pandas as pd

transacoes = pd.read_csv("../../dados/transacoes.csv", sep=";")
transacoes.head()

# %%

transacoes_produtos = pd.read_csv("../../dados/transacao_produto.csv", sep=";")
transacoes_produtos.head()

# %%

produtos = pd.read_csv("../../dados/produtos.csv", sep=";")
produtos.head()

# %%

import numpy as np

df_full = (transacoes.merge(transacoes_produtos,
                            how="left",
                            left_on="IdTransacao",
                            right_on="IdTransacao")
                     .merge(produtos, on="IdProduto")
                     .groupby(by="DescNomeProduto", as_index=False)
                     .agg({"IdTransacao":"count", "QtdePontos":[np.sum, np.mean]})
                    # .agg(
                    #     qtdeTransacao=("IdTransacao","count"),
                    #     totalPontos=("QtdePontos","sum"),
                    #     avgPontos=("QtdePontos","mean"),
                    # )
)

# %%

df_full.to_parquet("relatorio_itens.parquet", index=False)

# %%

df_full.to_pickle("relatorio_itens.pkl")