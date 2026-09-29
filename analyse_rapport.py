"""
Devoir Base de données & Data Science
Sujet : Expliquer la fermeture d'un grand nombre d'entreprises au Maroc

Ce script :
  1. importe le dataset (dataset.csv) : défaillances d'entreprises au Maroc, 2023-2025
  2. génère un graphique (graphique.png)

Sources des données : voir la colonne 'source' de dataset.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

# 1. Importer les données
df = pd.read_csv("dataset.csv")
print(df[["annee", "defaillances_entreprises", "variation_pct"]])

# 2. Construire le graphique
fig, ax = plt.subplots(figsize=(8, 5))

couleurs = ["#f97316" if v > 0 else "#16a34a" for v in df["variation_pct"]]
barres = ax.bar(df["annee"].astype(str), df["defaillances_entreprises"], color=couleurs)

ax.set_ylabel("Nombre de défaillances d'entreprises")
ax.set_xlabel("Année")
ax.set_title("Défaillances d'entreprises au Maroc (2023-2025)")
ax.set_ylim(0, df["defaillances_entreprises"].max() * 1.2)

# Valeurs et variations annuelles au-dessus des barres
for barre, valeur, variation in zip(barres, df["defaillances_entreprises"], df["variation_pct"]):
    ax.text(barre.get_x() + barre.get_width() / 2, barre.get_height() + 250,
            f"{valeur:,}\n({variation:+.1f} %)".replace(",", " "),
            ha="center", fontsize=9)

plt.tight_layout()
plt.savefig("graphique.png", dpi=150)
print("Graphique enregistré : graphique.png")
