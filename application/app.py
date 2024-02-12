import streamlit as st

from plot_utils import *

df_clean = pd.read_csv("./data/df_clean.csv")

st.title('World Happiness Report Data Visualization')

st.write("""
         Ceci est une visualisation des données extraites du World 
         Happiness Report, un sondage mondial sur l'état du bonheur 
         global. Le rapport classe 156 pays par leur niveau de bonheur, 
         mesuré par des facteurs tels que le PIB par habitant, le 
         soutien social, l'espérance de vie en bonne santé, la 
         liberté de faire des choix de vie, la générosité et la 
         perception de la corruption. Cette visualisation se concentre 
         sur la répartition des scores de bonheur par région.
         """)

st.markdown("## Classement des pays par score de bonheur")
st.plotly_chart(CountryHistogram(df_clean))
st.plotly_chart(Scatter(df_clean))

st.markdown("## Zoom sur les régions du monde")
st.plotly_chart(BoxPlotRegion(df_clean))

region = st.selectbox(label='Selectionner une région du monde',
                      options=["Monde", "Europe", "Afrique", "Asie"])
variable = st.selectbox(label='Selectionner une variable',
                        options=["Générosité",
                                 "Score de Bonheur",
                                 "Espérance de vie en bonne santé",
                                 "Assistance Sociale",
                                 "Liberté des choix"])

st.plotly_chart(WorldMap(df_clean, region, variable))

st.markdown("## Zoom sur les pays")

pays = st.selectbox(label='Selectionner un pays',
                    options=df_clean["Country name"].values)
st.plotly_chart(IndividualCountrySummary(df_clean, pays))

st.table(SummaryTable(df_clean, country=pays))
