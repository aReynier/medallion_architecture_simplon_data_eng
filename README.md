# Medallion architecture

Pour instalelr les dépendances:
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