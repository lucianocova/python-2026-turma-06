# %%

import pandas as pd

pd.options.display.max_rows = 150

df = pd.read_csv("../../dados/produtos.csv", sep=';')
df

# %%

df.isna().mean()

# %%

df.dropna(axis=1)

# %%

df.dropna(subset=["DescDescricaoProduto"],  axis=0, how='any')

# %%

df.fillna("FODASE")

# %%

df_teo = pd.DataFrame(
    {
        "nomes": ["teo", "nah", "mah", "teo", "mah"],
        "sobrenomes": [None, "ataide", "calvo", "calvo", "calvo"],
        "idades": [33, 35, None, 33, 4],
        "salario": [12342, 3500, None, None, 9837],
        "altura": [1.82, 1.67, 1.67, 1.92, 1.53],
        "dt_atualizacao": ["2026-01-01", "2026-05-01", "2026-06-02", "2026-06-01", "2026-06-02"],
    }
)

df_teo

# %%

df_teo_fill = df_teo.fillna( {
    "sobrenomes": "desconhecido",
})

df_teo_fill
# %%

medias = df_teo_fill[['salario', 'idades', "altura"]].mean()
medias

# %%
df_teo_fill.fillna(medias)
