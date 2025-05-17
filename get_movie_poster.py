# %%
import pandas as pd

# %%
# Chargement du fichier CSV
links_df = pd.read_csv("links.csv")
print(links_df.info())

# %%
# Conversion de l'ID IMDb au format tt0000000
links_df["imdb_id"] = links_df["imdbId"].apply(lambda x: f"tt{x:07d}")
print(links_df.head())

# %%
# URL IMDb (page du film)
links_df["imdb_url"] = links_df["imdb_id"].apply(lambda x: f"https://www.imdb.com/title/{x}")
print(links_df.head())

# %%
# URL de l'affiche (via OMDb)
OMDB_API_KEY = "f6ff1507"  # cle api demande et recu par mail
links_df["poster_url"] = links_df["imdb_id"].apply(
    lambda x: f"https://img.omdbapi.com/?i={x}&apikey={OMDB_API_KEY}"
)
print(links_df.head())

# %%
print(links_df['imdb_url'][0])
print(links_df['poster_url'][0])
# %%
# Sauvegarde au format Parquet
links_df.to_parquet("links_enriched.parquet", index=False)

print("Fichier enrichi sauvegardé dans output/links_enriched.parquet")


# %%