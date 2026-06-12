# %%

import pandas as pd

# %%

df_calvo = pd.DataFrame(
    {
        "idade": [33, 3, 31],
        "sobrenome": ["calvo", "calvo", "calvo"],
        "nome": ["teo", "maria", "lara"],
    }
)
df_calvo
# %%

df_ataide = pd.DataFrame(
    {
        "nome": ["nah", "maria", "bia", "natal"],
        "sobrenome": ["ataide", "ataide", "ataide", "ataide"],
        "idade": [35, 3, 30, 63],
        "salario": [3500, 300, 1230, 6233],
    }
)

df_ataide

# %%

df_balbino = pd.DataFrame(
    {
        "nome": ["tania", "nega"],
        "sobrenome": ["balbino", "balbino"],
    }
)

df_balbino_idade_salario = pd.DataFrame(
    {
        "idade": [35, 3, 1],
        "salario": [3500, 300,0],
    }
)

df_balbino_idade_salario = df_balbino_idade_salario.sort_values("salario")
df_balbino_idade_salario
# %%

pd.concat([df_calvo, df_ataide, df_balbino]).reset_index(drop=True)

# %%

pd.concat([df_balbino, df_balbino_idade_salario], axis=1)