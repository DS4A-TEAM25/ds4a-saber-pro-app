import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

#Read in data
df = pd.read_csv('pro.csv', low_memory=False)


#Define variables you wanna plot
variables = ['inst_caracter_academico', 'inst_origen',
          'estu_comocapacitoexamensb11',
          'estu_metodo_prgm', 'periodo', 'estu_genero']

####LAYOUT
# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(children='SABER PRO AT A GLANCE'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualizing the relationship between SABER PRO Scores and student variables'), className="mb-4")
        ]),
# choose between cases or deaths
    dcc.Dropdown(
        id='scores',
        options=[
            {'label': 'Razonamiento Cuantitativo', 'value': 'mod_razona_cuantitat_punt'},
            {'label': 'Lectura Critica', 'value': 'mod_lectura_critica_punt'},
            {'label': 'Competencia Ciudadana', 'value': 'mod_competen_ciudada_punt'},
            {'label': 'Ingles', 'value': 'mod_ingles_punt'},
            {'label': 'Comunicacion Escrita', 'value': 'mod_comuni_escrita_punt'},
        ],
        value='mod_razona_cuantitat_punt',
        #multi=True,
        style={'width': '50%'}
        ),
# for some reason, font colour remains black if using the color option
    dbc.Row([
        dbc.Col(dbc.Card(html.H4(children='Summary of Score',
                                 className="text-center text-light bg-dark"), body=True, color="dark")
        , className="mt-4 mb-4")
    ]),
    dbc.Row([
        dbc.Col(html.H5(children='Distribution of Score', className="text-center"),
                         width=4, className="mt-4"),
        dbc.Col(html.H5(children='Score over Period', className="text-center"), width=8, className="mt-4"),
        ]),


   #1ST GROUP OF GRAPHS     
        
    dbc.Row([
        dbc.Col(dcc.Graph(id='histogram_score'), width=5),
        dbc.Col(dcc.Graph(id='line_score_over_period'), width=7)
        ]),

  ####      
    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Relationship between Score and Selected Variables',
                                 className="text-center text-light bg-dark"), body=True, color="dark")
        , className="mb-4")
        ]),

    dcc.Dropdown(
        id='varsx',
        options=[{'label': i, 'value': i} for i in variables],
        value=['estu_metodo_prgm'],
        multi=False,
        style={'width': '70%', 'margin-left': '5px'}
    ),

    dbc.Row([
        dbc.Col(html.H5(children='Boxplot', className="text-center"),
                className="mt-4"),
    ]),

#2ND GROUP OF GRAPHS          
        
    dcc.Graph(id='box_plot_score_v_var'),

])


])



#### PAGE CALLBACKS
@app.callback(Output('histogram_score', 'figure'),
              [Input('scores', 'value')])


def update_histogram(scores):
    fig = go.Figure(data=[go.Histogram(x=df[scores])])
    
    fig.update_layout(yaxis_title='',
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       template = "seaborn",
                       margin=dict(t=0))
    
    return fig



@app.callback(Output('line_score_over_period', 'figure'),
              [Input('scores', 'value')])


def update_line(scores):
    db_sub = pd.DataFrame(df[scores].groupby(df['periodo']).mean())
    fig2 = go.Figure(go.Scatter(x=db_sub.index,y=db_sub[scores],
                                 name="",
                                 mode='markers+lines'))
    
    fig2.update_layout(yaxis_title='',
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       template = "seaborn",
                       margin=dict(t=0), 
                       yaxis=dict(range=[50,250]))
    
    return fig2


@app.callback(Output('box_plot_score_v_var', 'figure'),
              [Input('scores', 'value'), 
              Input('varsx', 'value')])


def update_boxplot(scores, varsx):
    
    fig3 = px.box(x=df[scores], y=df[varsx])
    
    
    fig3.update_layout(yaxis_title='',
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       margin=dict(t=0))
    
    return fig3








      
