import pandas as pd

nodes_df = pd.read_csv('data/raw/nodes.csv')
nodes_df.to_parquet('data/bronze/nodes.parquet')

edges_df = pd.read_csv('data/raw/edges.csv')
edges_df.to_parquet('data/bronze/edges.parquet')
