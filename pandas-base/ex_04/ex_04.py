# 04.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
# %%
import pandas as pd

df = pd.read_csv("../../dados/clientes.csv", sep=";")
df.head()
# %% MARIO
df.sort_values(by="qtdePontos", ascending=False)['idCliente'].head(1)

# %% MENOR
df.sort_values(by=["qtdePontos", "DtAtualizacao"], ascending=[True, False]).head(3)

# %%
# 225    0914dc1f-7f37-46b4-a9f3-a484b47449d2
