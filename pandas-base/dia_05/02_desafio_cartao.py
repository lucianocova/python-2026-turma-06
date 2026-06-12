# %%

import pandas as pd

import datetime

from dateutil.relativedelta import relativedelta

df = pd.read_csv("../../dados/cartao_credito.csv",sep=",")

df["dt"] = pd.to_datetime(df["dt"])
df["valor_parcela"] = df["valor"] / df["parcelas"]
df
# %%
df["dt_parcela"] = df.apply(lambda row: [(row["dt"] + relativedelta(months=1+i)).date() for i in  range(0,row["parcelas"])],
         axis=1)

# %%
df_explode = df.explode("dt_parcela")
df_explode["dt_fatura_mes"] = pd.to_datetime(df_explode["dt_parcela"]).dt.to_period("M")
df_explode

# %%
df_explode.pivot_table(index="dt_fatura_mes", values="valor_parcela", aggfunc="sum"  )

# %%

dt = datetime.datetime.now().date()
[ dt + relativedelta(months=1+i) for i in range(6) ]