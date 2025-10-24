# Medallion architecture
Ce projet a pour but de mettre en place une architecture en médaillon et de construire les différentes couches de cette architecture afin d'en comprendre son fonctionnement.

Pour installer les dépendances:
```
pip install -r requirements.txt
```

## Raw data
Script pour générer les données synthétisées:
```
python3 scripts/generate_sample_data.py
```

## Bronze data
Script pour convertir les fichiers CSV en parquet:
```
python3 scripts/to_parquet.py   
```
## Silver data
Script pour partitionner les edges et copier les nodes en silver:
```
python3 scripts/partition_edges.py
```

## Gold data
Script pour convertir les données silver en csv gold, prêt à l'emploi pour Neo4j:
```
python3 scripts/from_parquet_to_csv.py
```