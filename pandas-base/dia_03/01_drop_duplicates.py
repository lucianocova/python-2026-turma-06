# %%

import pandas as pd

df = pd.DataFrame(
    {
        "nomes": ["teo", "nah", "mah", "teo", "mah"],
        "sobrenomes": ["calvo", "ataide", "calvo", "calvo", "calvo"],
        "idades": [33, 35, 4, 33, 4],
        "dt_atualizacao": ["2026-01-01", "2026-05-01", "2026-06-02", "2026-06-01", "2026-06-02"],
    }
)

df

# %%

df.drop_duplicates(keep="last")

# %%

df.drop_duplicates(subset=["nomes"], keep='last', inplace=True)

# %%

df.sort_values(by="dt_atualizacao").drop_duplicates(subset=["nomes","sobrenomes"], keep="last")

# %%

df.sort_values(by=["nomes", "dt_atualizacao"]).drop_duplicates(subset=['sobrenomes'], keep="last")