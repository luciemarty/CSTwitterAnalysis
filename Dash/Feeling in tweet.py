import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Sentiment communiqué par les Tweets de 4 personnalités politiques'),

    html.Div(children='''
        Chaque personnalité a un numéro attribué:
        Numéro 1 pour Obama,
        Numéro 2 pour Trump,
        Numéro 3 pour May,
        Numéro 4 pour Trudeau,
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4], 'y': [0.36, 0.445, 0.37, 0.245], 'type': 'bar', 'name': u'Positive'},
                {'x': [1, 2, 3, 4], 'y': [0.605, 0.5, 0.6, 0.735], 'type': 'bar', 'name': u'Neutral'},
                {'x': [1, 2, 3, 4], 'y': [0.035, 0.055, 0.03, 0.02], 'type': 'bar', 'name': u'Negative'},
                {'x': [1, 2, 3, 4], 'y': [0.3674787427849929, 0.4648533531746033, 0.3839731337181337, 0.25482609126984124], 'type': 'bar', 'name': u'Subjectivity'},
            ],
            'layout': {
                'title': 'Analyse des tweets des personnalités via TextBlob - Echantillon de 200 tweets par personnalité'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
