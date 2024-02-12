import plotly.express as px
import plotly.graph_objs as go

regions_dic = {"Monde": "world",
               "Europe": "europe",
               "Afrique": "africa",
               "Asie": 'asia'}

features_dic = {"Générosité": "Generosity",
                "Score de Bonheur": "Ladder score",
                "Espérance de vie en bonne santé": "Healthy "
                                                   "life expectancy",
                "Assistance Sociale": "Social support",
                "Liberté des choix": "Freedom to make life choices"}


def BoxPlotRegion(df):
    fig = px.box(df, y="Regional indicator", x="Ladder score",
                 title="Boxplot du score de bonheur par région",
                 labels={"region": "Pays",
                         "Ladder score": "Score de Bonheur"},
                 orientation="h",
                 color_discrete_sequence=px.colors.sequential.Greens_r)
    return (fig)


def CountryHistogram(df):
    fig = px.histogram(df, x='Country name', y='Ladder score',
                       labels={'Ladder score': 'Score de bonheur'},
                       title="Distribution des scores du bonheur "
                             "de l'ensemble des pays")
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    fig.update_layout(yaxis_title='Pays',
                      xaxis_title='Score de Bonheur',
                      title_font_size=20)

    return (fig)


def Scatter(df):
    fig = px.scatter(df,
                     x="Ladder score",
                     y='Logged GDP per capita',
                     title="Distribution des pays par PIB par "
                           "habitant et score de bonheur",
                     hover_name='Country name')
    return (fig)


def WorldMap(df, region, variable):
    gdp_world_map = px.choropleth(df,
                                  locations="alpha-3",
                                  color=features_dic[variable],
                                  scope=regions_dic[region],
                                  title=f"Classement par {variable} "
                                        f"- {region}",
                                  color_continuous_scale="rdylgn",
                                  hover_name="Country name")

    gdp_world_map.update_layout(
        width=800,
        height=720,
        geo=dict(
            showframe=False,
            projection_type='equirectangular'
        ))

    return (gdp_world_map)


def IndividualCountrySummary(df, country):
    categories = ['PIB par tête', 'Assistance Sociale',
                  'Espérance de vie en bonne santé',
                  'Liberté des choix',
                  'Générosité', 'Perception de la corruption']

    list_of_columns = ['Explained by: Log GDP per capita',
                       'Explained by: Social support',
                       'Explained by: Healthy life expectancy',
                       'Explained by: Freedom to make life choices',
                       'Explained by: Generosity',
                       'Explained by: Perceptions of corruption']

    values_region = list(df.loc[df["Country name"] == country,
                        list_of_columns].values)[0]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values_region,
        theta=categories,
        fill='toself',
        name=country
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 2]
            )),
        showlegend=True)

    return (fig)


def SummaryTable(df, country):
    list_of_columns = ['Country name', 'rank', 'Ladder score',
                       'Explained by: Log GDP per capita',
                       'Explained by: Social support',
                       'Explained by: Healthy life expectancy',
                       'Explained by: Freedom to make life choices',
                       'Explained by: Generosity',
                       'Explained by: Perceptions of corruption']

    table = df.loc[df["Country name"] == country, list_of_columns]
    table = table.rename(columns={'Country name': "Pays",
                                  'rank': "Classement (en termes "
                                          "de Bonheur)",
                                  'Ladder score': "Score de Bonheur",
                                  'Explained by: Log GDP per capita':
                                      "Expliqué par le PIB par tête",
                                  'Explained by: Social support':
                                      "Expliqué par l'assistance sociale",
                                  'Explained by: Healthy life '
                                  'expectancy': "Expliqué par "
                                                "l'epsérance de vie "
                                                "en bonne santé",
                                  'Explained by: Freedom to make life '
                                  'choices': "Expliqué par la liberté "
                                             "de choix",
                                  'Explained by: Generosity':
                                      "Expliqué par la générosité",
                                  'Explained by: Perceptions of '
                                  'corruption': "Expliqué par la "
                                                "perception de"
                                                " corruption"})

    table = table.transpose()
    table.columns = ["Résumé"]
    return (table)
