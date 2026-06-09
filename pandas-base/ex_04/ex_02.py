# 04.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova

# %%

import pandas as pd
import numpy as np

# %%

df = pd.read_csv("../../dados/clientes.csv", sep=";")

# %%
np.log(df["qtdePontos"]+1)
