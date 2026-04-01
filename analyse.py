import pandas as pd

# Chargement des données
df = pd.read_parquet('../data/assurances_enrichi.parquet')

# Calcul de la prime moyenne
prime_moy = df['Prime_estimee'].mean()
print(f"Prime moyenne : {prime_moy:.2f} €")
