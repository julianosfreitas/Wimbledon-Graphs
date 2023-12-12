from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# Pegar as infromações da tabela do Excel
df = pd.read_excel("AcesAll.xlsx")                      # ACES ALL TIMES
df2 = pd.read_excel("PointsPerGameAll.xlsx")            # POINTS PER GAME ALL TIMES
df3 = pd.read_excel("TotalGamesWonAll.xlsx")            # GAMES WON ALL TIMES
df4 = pd.read_excel("TotalPointsWonAll.xlsx")           # POINTS TOTAL ALL TIMES
df5 = pd.read_excel("SetsWonAll.xlsx")                  # SETS WON ALL TIMES

#Fazendo o Gráfico
fig = px.scatter(df, x="Atleta", y="Aces", color="ID do País")
fig2 = px.scatter(df2, x="Atleta", y="Pontos por Jogo", color="ID do País")
fig3 = px.scatter(df3, x="Atleta", y="Jogos Ganhos", color="ID do País")
fig4 = px.scatter(df4, x="Atleta", y="Total de Pontos", color="ID do País")
fig5 = px.scatter(df5, x="Atleta", y="Sets Ganhos", color="ID do País")

''' 
opcoes = list(df["name"].unique())
opcoes.append("TODOS OS ATLETAS")
'''

# Enfeite :)
app.layout = html.Div(children=[
    html.H1(children='ALL TIMES WIMBLEDON STATS'),

    html.Div(children='''
        Obs: Esse gráfico mostra as estatiscicas de todos os tempos.
    '''),

     # dcc.Dropdown(opcoes, value='TODOS OS ATLETAS', id='lista_atletas'),

    # Chamando o Gráfico
    dcc.Graph(
        id='grafico_aces',
        figure=fig
    ),
    dcc.Graph(
        id='grafico_points_per_game',
        figure=fig2
    ),
    dcc.Graph(
        id='grafico_games_won',
        figure=fig3
    ),
    dcc.Graph(
        id='grafico_points_total',
        figure=fig4
    ),
    dcc.Graph(
        id='grafico_sets_won',
        figure=fig5
    )
])

# Escolha do atleta expecifico
'''
@app.callback(
    Output('grafico_aces', 'figure'),
    Input('lista_atletas', 'value')
)
def update_output(value):
    if value == "TODOS OS ATLETAS":
        fig = px.scatter(df, x="name", y="value", color="country_id")
        
    else:
        tabela_filtrada = df.loc[df['name']==value, :]
        fig = px.scatter(tabela_filtrada, x="name", y="value", color="country_id")
        
    return fig
'''

if __name__ == '__main__':
    app.run(debug=True)
