import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import textwrap #
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_table as dt
import numpy as np



from app import app

#Read in data
df = pd.read_csv('pro.csv', low_memory=False)

#Define variables for reactive components
period = df['periodo'].unique()

departamento_options = df['estu_inst_departamento'].dropna().unique()

wrapper = textwrap.TextWrapper(width=11) #Text wrapper so that long labels are wrapped in legend

var_options = ("estu_genero", "estu_areareside", "estu_pagomatriculabeca", "estu_pagomatriculacredito", "estu_pagomatriculapadres",
"estu_pagomatriculapropio", "estu_comocapacitoexamensb11", "fami_hogaractual", "fami_cabezafamilia", "fami_numpersonasacargo",
"fami_educacionpadre", "fami_educacionmadre", "fami_ocupacionpadre", "fami_ocupacionmadre", "fami_estratovivienda", "fami_personashogar",
"fami_cuartoshogar", "fami_tieneinternet", "fami_tienecomputador", "fami_tienelavadora", "fami_tienehornomicroogas", "fami_tienetelevisor",
"fami_tieneautomovil", "fami_tienemotocicleta", "fami_numlibros", "estu_dedicacionlecturadiaria", "estu_dedicacioninternet", "estu_prgm_academico")

####STYLES: (this should be in a css file but will leave here so that changes can be made more easily, then move)
#Style: move this to somewhere else so that you can use it on all pages
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    'border-radius': '5px',
    "width": "18rem",
    'background-color': '#f9f9f9',
    'margin': '20px',
    'padding': '15px',
    'position': 'fixed',
    'box-shadow': '2px 2px 2px lightgrey'
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'position': 'relative',
}


mini_container = {
  'border-radius': '5px',
  'background-color': '#f9f9f9',
  'margin': '10px',
  'padding': '15px',
  'position': 'relative',
  'box-shadow': '2px 2px 2px lightgrey'
}

pretty_container = {
  'border-radius': '5px',
  'background-color': '#f9f9f9',
  'margin': '10px',
  'padding': '15px',
  'position': 'relative',
  'box-shadow': '2px 2px 2px lightgrey',
}


#Tokens in case mapbox is used
mapbox_access_token =""


#Possible layout to use for map
layout_map = {
    'autosize':True,
    'automargin':True,
    'margin': {'l':30, 'r':30, 'b':20, 't':40},
    'hovermode': "closest",
    'plot_bgcolor': "#F9F9F9",
    'paper_bgcolor': "#F9F9F9",
    'legend': {'font':{'size':10}, 'orientation':'h'},
    'title':'Colombia Map',
    'mapbox':{
     'accesstoken': mapbox_access_token,
        'style':"light",
        'center': {'lon':-78.05, 'lat':42.54},
        'zoom':7
    }
}





##################### Layout ######################################


layout = html.Div(
    [
html.Div(
    [
        #SIDEBAR
        
        html.H4("Explore by Department", className="display-4", 
                   style = {'font-size': '36px'}),
        html.Hr(),
        
        #Period
        html.P(
            "Period", className="lead"
        ),
        dcc.RangeSlider(
            marks={2016: '2016',
                   2017: '2017',
                   2018: '2018',
                   2019: '2019'
                  },
            id='period-slider',
            step=1,
            min=2016,
            max=2019,
            value=[2016, 2019], 
            className= "mb-5"
        ),  
        
        #Department
        html.P(
            "Department", className="lead"
        ),
        dcc.Dropdown(
        id='departamentos',
        options=[{'label': i, 'value': i} for i in departamento_options],
        placeholder="Select a Department",  
        multi=False,
        className= "mb-4",    
        optionHeight=80,
        style={'width': '100%'}
        ), 
        
        
        #Score
        html.P(
            "Saber PRO Score", className="lead"
        ),
        dcc.Dropdown(
        id='scores',
        options=[
            {'label': 'Quantitative Reasoning', 'value': 'mod_razona_cuantitat_punt'},
            {'label': 'Critical Reading', 'value': 'mod_lectura_critica_punt'},
            {'label': 'Citizenship Competence', 'value': 'mod_competen_ciudada_punt'},
            {'label': 'English', 'value': 'mod_ingles_punt'},
            {'label': 'Writing', 'value': 'mod_comuni_escrita_punt'},
        ],
        placeholder="Select a Score",    
        multi=False,
        className= "mb-4",  
        style={'width': '100%'}
        ), 
        
         #Var 1
        html.P(
            "Variables", className="lead"
        ),
        dcc.Dropdown(
        id='variables',
        options=[{'label': i, 'value': i} for i in var_options],
        placeholder="Select a Variable", 
        multi=False,
        className= "mb-4",      
        style={'width': '100%'}
        ), 

        
    ],
    style=SIDEBAR_STYLE,
   
),
        html.Div(
        [

            #row1
            dbc.Row(
            [
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="avg_dpt_text"), 
                    
                    html.P(
                    html.Span("Average Score at Department", id="tooltip-avg_dpt",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Average value of selected score at Department.", target="tooltip-avg_dpt", placement="bottom")
                ],
                id="avg_dpt", style = mini_container
                                ))),
                
                
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="avg_col_text"), 
                     html.P(
                    html.Span("Average Score Colombia", id="tooltip-avg_col",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Average value of selected score across all departments in Colombia", target="tooltip-avg_col", placement="bottom")
                ],
                id="avg_col", style = mini_container
                                ))),
                
                
                
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="rank_text_dpt"), 
                    html.P(
                    html.Span("Rank", id="tooltip-rank_dpt",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Ranking of the Department on the selected score", target='tooltip-rank_dpt', placement="bottom")
                ],
                id="rank_dpt", style = mini_container
                                ))),
            ],
            
            
        ), 
                    
                    
             #row2
            dbc.Row(
            [
                dbc.Col(
                        
                        [dcc.Graph(id="map")],
                            id="map_container",
                        
                        style = pretty_container),
                
                
                dbc.Col(html.Div(id="dt_department"
                
                
                    
                )
                    , style = pretty_container),
            ]
        ),
            

            
            #row3
            
            
            
           
            
            
            
        
            
        ], 
            style= CONTENT_STYLE
        
        
        ) 
        
         
        
        
    ]
)


##################### Callbacks ######################################