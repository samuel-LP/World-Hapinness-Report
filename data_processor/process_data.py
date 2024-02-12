import pandas as pd

##################### Import des données #########################

df = pd.read_csv("./data/WorldHapiness.csv")
mapping = pd.read_csv("./data/Mapping.csv")
print("Données Importées ✅")

######################## Nettoyage des données #######################

df['rank'] = df['Ladder score'].rank(ascending=False)
df['rank'] = df['rank'].astype(int)
mapping = mapping.rename(columns={"name": "Country name"})

mapping = mapping[
    ["Country name", "alpha-2", "alpha-3", "iso_3166-2"]]
mapping.loc[mapping[
                "Country name"] == "Russian Federation",
"Country name"] = "Russia"
mapping.loc[mapping[
                "Country name"] == ("United Kingdom of Great Britain "
                                    "and Northern Ireland"),
"Country name"] = "United Kingdom"
mapping.loc[mapping[
                "Country name"] == "Czechia", "Country name"] = \
    "Czech Republic"
mapping.loc[mapping[
                "Country name"] == "Bolivia (Plurinational State of)",
"Country name"] = "Bolivia"
mapping.loc[
    mapping["Country name"] == "Viet Nam", "Country name"] = "Vietnam"
mapping.loc[mapping[
                "Country name"] == "Iran (Islamic Republic of)",
"Country name"] = "Iran"
mapping.loc[mapping[
                "Country name"] == ("Venezuela (Bolivarian Republic of)"
                                    ""), "Country name"] = "Venezuela"
mapping.loc[mapping[
                "Country name"] == "United States of America",
"Country name"] = "United States"
mapping.loc[mapping[
                "Country name"] == ("Congo, Democratic Republic of "
                                    "the"), "Country name"] = \
    "Congo (Kinshasa)"
print("Feature Engineering terminé ✅")

df_clean = df.merge(mapping, on='Country name', how='left')

#####################  Sauvegarde des données ####################

df_clean.to_csv("./data/df_clean.csv")
print("Données sauvegardées ✅")
