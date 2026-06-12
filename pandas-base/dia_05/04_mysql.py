# %%

import pandas as pd
import sqlalchemy

import dotenv
dotenv.load_dotenv(".env")

import os

os.getenv("PATH")

# %%
USER_DB = os.getenv("USER_DB")
PASS_DB = os.getenv("PASS_DB")
URI_DB = os.getenv("URI_DB")
NAME_DB = os.getenv("NAME_DB")

uri = f"mysql+pymysql://{USER_DB}:{PASS_DB}@{URI_DB}/{NAME_DB}?charset=utf8mb4"
engine = sqlalchemy.create_engine(uri)

# %%
df = pd.read_sql("transactions", engine)
df.head()

# %%

df.shape

# %%

query = """

SELECT id_customer,
         COUNT(uuid),
         SUM(vl_points)
FROM transactions
GROUP BY 1
order by 3 DESC
"""

df = pd.read_sql(query, engine)
df.head()

# %%

uri = f"mysql+pymysql://{USER_DB}:{PASS_DB}@{URI_DB}/{NAME_DB}?charset=utf8mb4"
engine = sqlalchemy.create_engine(uri)
engine_sqlite = sqlalchemy.create_engine("sqlite:///../../dados/database.db")

df = pd.read_sql("transactions", engine)
df.to_sql("transactions", engine_sqlite, index=False)