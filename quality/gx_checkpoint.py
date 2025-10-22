import pandas as pd

nodes_df = pd.read_parquet('data/bronze/nodes.parquet')
edges_df = pd.read_parquet('data/bronze/edges.parquet')

if nodes_df.id.is_unique is False:
    raise ValueError("All the ID aren't unique value")

if edges_df.src.isnull().values.any() is True:
    raise ValueError("At least ont src value is NULL")

if edges_df.dst.isnull().values.any() is True:
    raise ValueError("At least ont dst value is NULL")
