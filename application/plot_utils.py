import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

def BoxPlotRegion(df):
    fig = px.box(df, y="Regional indicator", x="Ladder score",
                 title="Happiness score boxplot by region",
                 labels={"region": "Region", "Ladder score": "Happiness Score"},
                 orientation="h",
                 color_discrete_sequence=px.colors.sequential.Greens_r)
    return(fig)
def CountryHistogram(df):
    fig = px.histogram(df, x='Country name', y='Ladder score',
                       labels={'Ladder score': 'Score du bonheur'},
                       title='Distribution des scores du bonheur des 10 meilleurs pays')
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)
    fig.update_layout(yaxis_title='Region', xaxis_title='Happiness Score', title_font_size=20)

    return (fig)

def Scatter(df):
    fig = px.scatter(df, x = "Ladder score", y = 'Logged GDP per capita', title="Scatter plot", hover_name='Country name')
    return(fig)

def WorldMap(df, region, variable):
    gdp_world_map = px.choropleth(df,
                                  locations="alpha-3",
                                  color=variable,
                                  scope=region,
                                  title=f"{variable} Ranking World Map",
                                  color_continuous_scale="rdylgn",
                                  hover_name="Country name")

    gdp_world_map.update_layout(
        width=800,
        height=720,
        geo=dict(
            showframe=False,
            projection_type='equirectangular'
        ))

    return(gdp_world_map)

def IndividualCountrySummary(df, country):
    categories = ['Log GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom to make life choices',
                  'Generosity', 'Perceptions of corruption']

    list_of_columns = ['Explained by: Log GDP per capita', 'Explained by: Social support',
                          'Explained by: Healthy life expectancy',
                          'Explained by: Freedom to make life choices',
                          'Explained by: Generosity', 'Explained by: Perceptions of corruption']

    values_region = list(df.loc[df["Country name"] == country, list_of_columns].values)[0]

    # Création du graphique
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
                range=[0, 2]  # Ajuster cette plage en fonction de vos données
            )),
        showlegend=True
    )

    return(fig)

def SummaryTable(df, country):
    list_of_columns = ['Country name', 'rank', 'Ladder score', 'Explained by: Log GDP per capita', 'Explained by: Social support',
                      'Explained by: Healthy life expectancy',
                      'Explained by: Freedom to make life choices',
                      'Explained by: Generosity', 'Explained by: Perceptions of corruption']

    table = df.loc[df["Country name"] == country, list_of_columns]
    table = table.transpose()
    table.columns = ["Summary"]
    return(table)


