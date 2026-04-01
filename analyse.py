
import pandas as pd

# Chargement des données
df = pd.read_parquet('../data/assurances_enrichi.parquet')

# Calcul de la prime moyenne globale
prime_moy = df['Prime_estimee'].mean()
print(f"Prime moyenne : {prime_moy:.2f} €")

# Calcul par région (ajout)
prime_region = df.groupby('Region_MAJ')['Prime_estimee'].mean().sort_values(ascending=False)
print(prime_region)
