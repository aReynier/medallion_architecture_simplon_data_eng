import os
import pandas as pd
import numpy as np

edges_df = pd.read_parquet('data/bronze/edges.parquet')
nodes_df = pd.read_parquet('data/bronze/nodes.parquet')


edges_shards_df = np.array_split( edges_df, 8)

for i, edges_shard_df in enumerate(edges_shards_df):
    if not os.path.isdir(f'data/silver/shard={i}'):
        os.makedirs(f'data/silver/shard={i}')
    edges_shard_df.to_parquet(f'data/silver/shard={i}/edges.parquet')


nodes_df.to_parquet('data/silver/nodes.parquet')