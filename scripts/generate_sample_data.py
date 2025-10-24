from faker import Faker
import polars as pl
import random


Faker.seed(42)
fake = Faker()

num_nodes = 1000000
num_edges = 5000000

def generate_nodes(num_nodes: int) -> pl.DataFrame:
        node_data = {
                "id": range(1, num_nodes + 1),
                "label": [fake.word(ext_word_list=['abc', 'def', 'ghi', 'jkl']) for _ in range(num_nodes)],
                "name": [fake.name() for _ in range(num_nodes)]
        }
        return pl.DataFrame(node_data)


def generate_edges(num_edges, num_nodes) -> pl.DataFrame:
        edge_data = {
                "src": [random.randint(1, num_nodes) for _ in range(num_edges)],
                "dst": [fake.word(ext_word_list=['123', '456']) for _ in range(num_edges)],
                "type": ["REL" for _ in range(num_edges)]
        }
        return pl.DataFrame(edge_data)


nodes_df = generate_nodes(num_nodes)
edges_df = generate_edges(num_edges, num_nodes)

edges_df = edges_df.unique()

nodes_df.write_csv("data/raw/nodes.csv")
edges_df.write_csv("data/raw/edges.csv")
