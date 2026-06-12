# %%

import pandas as pd

import os

folder = "../../dados/ipea/"

dfs = []
for file_name in os.listdir(folder):
    df = pd.read_csv(folder + file_name, sep=";")
    df = (df.set_index(["nome","período"])
            .rename(columns={"valor":file_name.split(".")[0]})
            .drop("cod", axis=1))
    dfs.append(df)

# %%

df_full = pd.concat(dfs, axis=1).reset_index()
df_full

# %%
