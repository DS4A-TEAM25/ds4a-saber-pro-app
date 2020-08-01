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
import json
from urllib.request import urlopen
from plotly.offline import plot
import plotly.io as pio
pio.renderers.default = 'browser' #prevent graphs from opening in other tabs
from sqlalchemy import create_engine


from app import app

#Load map
with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    colombia = json.load(response)
    
#Mapbox Token
token = "pk.eyJ1IjoibXBhcm9jYSIsImEiOiJja2NpZjUwczEwaGVvMnF1OWM2OGNxOHZkIn0.EVHh5zRvHQBD-PcIU1flEw"    
    
#Read in data from rds
engine = create_engine('postgresql://admin:ds4a@data-team25.c6tqz0tiazsw.us-east-2.rds.amazonaws.com/project_ds4a')

#df = pd.read_sql("SELECT * FROM pro", engine.connect())

#df = pd.read_csv('pro.csv', low_memory=False)    

#Define variables for reactive components

#Department options
#departamento_options = df['estu_inst_departamento'].dropna().unique() #QUERY

departamento_options = pd.read_sql("SELECT DISTINCT estu_inst_departamento FROM PRO", engine.connect())
departamento_options = departamento_options['estu_inst_departamento']

wrapper = textwrap.TextWrapper(width=11) #Text wrapper so that long labels are wrapped in legend

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
            id='period_slider',
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



###MAP

@app.callback(Output("map", "figure"), [Input("scores", "value"), 
                                       Input("period_slider", "value")])

def plot_score_choro_state(scores, period_slider):
    
    if scores is None:
        return {"layout": {
            "xaxis": {
                "visible": False
            },
            "yaxis": {
                "visible": False
            },
            'title': {
                'text' : '<b>Scores Across Deparments:</b><br>' + 'Select a Score'
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }
    
    else:
        #mean_score = df.groupby('estu_inst_departamento')[scores].agg(mean_score=('mean')) #####QUERY
        #mean_score.index.names = ['Department']
        
        
        
        mean_score = pd.read_sql("SELECT estu_inst_departamento,AVG(CAST ( "+scores+" AS DOUBLE PRECISION)) mean_score FROM avg_score WHERE periodo BETWEEN '"+str(period_slider[0])+ "' AND '" +str(period_slider[1])+"'  GROUP BY estu_inst_departamento", engine.connect())
        mean_score = mean_score.set_index("estu_inst_departamento")
        mean_score = mean_score.rename(index={'BOGOTA': 'SANTAFE DE BOGOTA D.C'}) #Changing names that are different in the json file and our data
        mean_score = mean_score.rename(index={'VALLE': 'VALLE DEL CAUCA'})
        mean_score = mean_score.rename(index={'NORTE SANTANDER': 'NORTE DE SANTANDER'})
        
        fig_map = go.Figure(data=go.Choroplethmapbox(
            locations=mean_score.index, # Spatial coordinates
            z = mean_score.mean_score, # Data to be color-coded
            geojson=colombia, 
            featureidkey = "properties.NOMBRE_DPT", # set of locations match entries in `locations`
            colorscale = "RdYlBu",
            marker_opacity=0.6,
            zmin=min(mean_score.mean_score),
            zmax=max(mean_score.mean_score),
            colorbar_title = 'Mean Score',
            marker_line_color='#395CA3', # line markers between states
        ))
        
        fig_map.update_layout(
            title_text = 'Mean Score across Departments',
            mapbox_style="mapbox://styles/mparoca/ckd9lvz570c4i1ippkzk9q8gq", mapbox_accesstoken=token,
            mapbox_zoom=4,
            mapbox_center = {"lat": 4.570868, "lon": -74.2973328}, 
            margin={"r":0,"t":0,"l":0,"b":0}
        )
        return fig_map
