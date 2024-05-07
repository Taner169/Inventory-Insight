import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import glob
import os
from mappLista import mapp_konfiguration

csv_mapp = 'csv_data'
app = dash.Dash(__name__)

mappar = list(mapp_konfiguration.keys())

def rensa_citationstecken(namn):
    return namn.replace('"', '').strip()

app.layout = html.Div([
    dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0),
    dcc.Dropdown(id='mapp-dropdown', options=[{'label': m, 'value': m} for m in mappar], value=mappar[0]),
    dcc.Input(id='artikel-sok', type='text', placeholder='Sök artikelnummer...'),
    html.Div(id='graph-container')
])

@app.callback(
    Output('graph-container', 'children'),
    [Input('mapp-dropdown', 'value'),
     Input('artikel-sok', 'value')]
)
def uppdatera_grafer(mapp, artikel_sok):
    lista_av_filer = glob.glob(os.path.join(csv_mapp, f'{mapp}_*.csv'))
    lista_av_dataframes = []
    for fil in lista_av_filer:
        df = pd.read_csv(fil)
        lista_av_dataframes.append(df)
    
    if lista_av_dataframes:
        df_concat = pd.concat(lista_av_dataframes)
        kolumn_artikel = rensa_citationstecken(mapp_konfiguration[mapp]['kolumner'][0])
        kolumn_saldo = rensa_citationstecken(mapp_konfiguration[mapp]['kolumner'][1])

        # Filtrera på artikelnummer om söksträngen är angiven
        if artikel_sok:
            df_concat = df_concat[df_concat[kolumn_artikel].astype(str).str.contains(artikel_sok)]

        # Skapa grafer baserat på filtrerade data
        fig1 = px.bar(df_concat, x=kolumn_artikel, y=kolumn_saldo, title='Saldo per Artikel')
        fig2 = px.histogram(df_concat, x=kolumn_saldo, title='Fördelning av Saldo')

        return html.Div([
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2)
        ])
    return html.Div("Ingen data tillgänglig.")

if __name__ == '__main__':
    app.run_server(debug=True)

