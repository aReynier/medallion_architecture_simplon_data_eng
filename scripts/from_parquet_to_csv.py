import pandas as pd
from pathlib import Path

nodes_df = pd.read_parquet('data/silver/nodes.parquet')


edges_directory = Path('data/silver')
full_deges_df = pd.concat(
    pd.read_parquet(parquet_file)
    for parquet_file in edges_directory.glob('shard=*/edges.parquet')
)


renamed_nodes_df = nodes_df.rename(columns={"id":"ID"})

renamed_edges_df = full_deges_df.rename(columns={"src":"START_ID", "dst":"END_ID"})
dropped_renamed_edges_df = renamed_edges_df.drop("type", axis=1)


nodes_gold_csv = renamed_nodes_df.to_csv("data/gold/nodes.csv", index=False)
edges_gold_csv = dropped_renamed_edges_df.to_csv("data/gold/edges.csv", index=False)
