# %%

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///../../dados/database.db")

# %%

df = pd.read_sql_table("transacoes", engine)
df

# %%
def import_query(path):
    with open(path, "r") as open_file:
        query = open_file.read()
    return query


query_all = import_query("query.sql")
print(query_all)

print("------")

query_usuarios = import_query("quantidade_usuarios.sql")
print(query_usuarios)

# %%

df = pd.read_sql_query(query_all, engine)
df