# %%

import pandas as pd

df_teo = pd.DataFrame(
    {
        "nomes": ["teo     balbino", "nah    giRONde", "mah", "teo", "mah"],
        "sobrenomes": [None, "ataide", "calvo", "calvo", "calvo"],
        "idades": [33, 35, None, 33, 4],
        "salario": [12342, 3500, None, None, 9837],
        "altura": [1.82, 1.67, 1.67, 1.92, 1.53],
        "dt_atualizacao": ["2026-01-01", "2026-05-01", "2026-06-02", "2026-06-01", "2026-06-02"],
    }
)

df_teo

# %%
df_teo.replace("calvo", "Calvo")

# %%

df_teo.replace(["calvo", "ataide", 12342.0], ["Calvo", "Ataide", 1232.0])

# %%

replace = {
    "calvo": "Calvo",
    "ataide": "Ataide",
    12342.0: 1232.0,
}

df_teo.replace(replace)

# %%

def format_txt(txt):
    txt_split = txt.split(" ")
    txt_split = [i for i in txt_split if i != '']
    return " ".join(txt_split).title()


df_teo["nomes"].apply(format_txt)

# %%
