import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import textwrap 
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
from utils import *
from textwrap import dedent
from sqlalchemy import create_engine

from app import app
    
#Load map
with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    colombia = json.load(response)
    
#Mapbox Token
token = "pk.eyJ1IjoibXBhcm9jYSIsImEiOiJja2NpZjUwczEwaGVvMnF1OWM2OGNxOHZkIn0.EVHh5zRvHQBD-PcIU1flEw"  


#Define variables for reactive components
#Departamento options
departamento_options = get_unique(engine, 'pro_data', "estu_inst_departamento")
departamento_options = sorted(departamento_options)

####STYLES:
# the style arguments for the sidebar
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

#Container styles
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
        
        
        #Score
        html.P(
            "Saber PRO Skill", className="lead"
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
        placeholder="Select a Skill", 
        multi=False,
        className= "mb-4",  
        style={'width': '100%'}
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
        
        
        
        
        
    ],
    style=SIDEBAR_STYLE,
   
),
        html.Div(
        [

            #row1
            dbc.Row(
            [
                #AVERAGE SCORE AT DEPARTMENT CARD
                
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
                
                
                #AVERAGE SCORE COLOMBIA CARD
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
                
                
                #RANK CARD
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
            
            #MAP
            dbc.Row(
            [
                dbc.Col(
                        
                        [dcc.Graph(id="map")],
                            id="map_container",
                        
                        style = pretty_container),
                
            #SCATTER PLOT    
                dbc.Col(
                
                    [
                        dbc.Button(
                            html.Span([html.I(className="fas fa-question-circle ml-0"), ""]), id="simple-toast-toggle5", color="#395CA3", outline=False),
                         dbc.Toast(
                             [html.P("The population of all Colombian students was divided into 5 groups, according to their score on the selected skill. Students that scored on the highest quintile of the distribution had the best performance, while students that score on the lowest quintile had the worst. This graph plots universities at the selected Department based on these score quintiles. Each observation represents a university within the selected department. The x-axis shows the percentage of students that scored on the lowest quintile (1st quintile). The y-axis shows the percentage of students that scored on the highest quintile(5th quintile). Ideally you want to have most of your students scoring in the 5th quintile, and very few scoring in the 1st", className="mb-0")],
                             id="simple-toast5",
                             header="Quintile Plot of Universities at Department",
                             icon="danger", is_open=False,
                             dismissable=True,
                         ),
                        
                        dcc.Loading(dcc.Graph(id="department_quantiles"), color="#395CA3", type="default")],
                            id="department_quantiles_Container",
                        
                        style = pretty_container),
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
                'text' : '<b>Map of Mean Score across Departments:</b><br>' + 'Select a Skill' 
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }
    
    else:
        
        p=[str(period_slider[0]), str(period_slider[1])] 
        
        mean_score = pd.read_sql("SELECT estu_inst_departamento,AVG("+scores+") mean_score FROM pro_data WHERE periodo BETWEEN '"+p[0]+ "' AND '" +p[1]+"'  GROUP BY estu_inst_departamento", engine.connect())
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
    
    

### AVERAGE SCORE OF DEPARTMENT CARD    
@app.callback(
    Output("avg_dpt_text", "children"),
    [
        Input("scores", "value"),
        Input("period_slider", "value"), 
         Input("departamentos", "value")
    ],
)


def update_avg_dpt(scores, period_slider, departamentos):
    
    if departamentos is None or scores is None:
        return []
    
    else:
        

        p=[str(period_slider[0]), str(period_slider[1])] 
        mean_dpt = get_avg(engine, 'pro_data', scores, "estu_inst_departamento", "'"+str(departamentos)+"'", "'"+p[0]+"'", "'"+p[1]+"'")
        if mean_dpt[0]!= None:
            return round(mean_dpt[0],2)
        else:
             return str("No Data for Selected Period")




### AVERAGE SCORE OF COLOMBIA
#avg_col
@app.callback(
    Output("avg_col_text", "children"),
    [
        Input("scores", "value"),
        Input("period_slider", "value")
    ],
)


def update_avg_col(scores, period_slider):
    
    if scores is None:
        return []
    
    else:
        p=[str(period_slider[0]), str(period_slider[1])] 
        mean_col = pd.read_sql("SELECT AVG("+scores+") AS mean_col FROM pro_data WHERE periodo BETWEEN '"+p[0]+ "' AND '" +p[1]+"'", engine.connect())
        return mean_col.mean_col[0].round(2)



### RANK
@app.callback(
    Output("rank_text_dpt", "children"),
    [
        Input("scores", "value"),
        Input("period_slider", "value"), 
         Input("departamentos", "value")
    ],
)


def update_rank(scores, period_slider, departamentos):
    
    if departamentos is None or scores is None:
        return []
    
    else:
        p=[str(period_slider[0]), str(period_slider[1])] 
        mean_score = pd.read_sql("SELECT estu_inst_departamento,AVG("+scores+") mean_score FROM pro_data WHERE periodo BETWEEN '"+p[0]+ "' AND '" +p[1]+"'  GROUP BY estu_inst_departamento", engine.connect())
        if len(mean_score[mean_score.estu_inst_departamento==departamentos])!= 0:
            mean_score  = mean_score .dropna()
            total_departments = str(len(mean_score['estu_inst_departamento'].unique()))
            mean_score = mean_score.sort_values(by='mean_score', ascending=False).reset_index(drop=True)
            mean_score.index = mean_score.index + 1
            return str(mean_score.index[mean_score.estu_inst_departamento==departamentos][0]) + "/" + total_departments
        else:
            return str("No Data for Selected Period")
        


#Scatter_department
@app.callback(
    Output("department_quantiles", "figure"),
    [
        Input("scores", "value"),
        Input("period_slider", "value"), 
         Input("departamentos", "value")
    ],
)

def update_university_quantiles(scores, period_slider, departamentos):

    if departamentos is None or scores is None:
        return {"layout": {
            "xaxis": {
                "visible": True, 
                'range': [1,80]
            },
            "yaxis": {
                "visible": True, 
                'range':[1,100]
            },
            'title': {
                'text' : '<b>Universities at ' + 'Selected Department' +  ' by Score Quintiles:</b><br>' + 'Select a Department and a Saber Pro Score'
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }
    
    else:
        quintile_score = 'quintile_' + scores
        p=[str(period_slider[0]), str(period_slider[1])] 
        quint_table = get_pct(engine, "pro_data", "inst_nombre_institucion", quintile_score, scores,"estu_inst_departamento", "'"+str(departamentos)+"'", "'"+p[0]+"'", "'"+p[1]+"'")
        quint_table = pd.DataFrame(quint_table, columns = ['inst_nombre_institucion', 'sum_quintil_1', 'sum_quintil_5', 'sum_students', 'avg_score'])
        quint_table['pct_quint1'] = round(quint_table['sum_quintil_1']/quint_table['sum_students'] * 100,2)
        quint_table['pct_quint5'] =round(quint_table['sum_quintil_5']/quint_table['sum_students'] * 100,2)
        
        
        figq = go.Figure()
        figq.add_trace(go.Scatter(
            x=quint_table['pct_quint1'] ,
            y=quint_table['pct_quint5'],
            hovertext=quint_table['inst_nombre_institucion'], 
            hoverlabel=dict(namelength=0),
            hovertemplate='%{hovertext}<br>1st Quintile: %{x}%  <br>5th Quintile: %{y}% ',
            mode='markers',
            marker_color="#395CA3"
        ))
       
        figq.add_shape(
        # Line Vertical
            dict(
                type="line",
                x0=20,
                y0=0,
                x1=20,
                y1=100,
                line=dict(color="black",
                          width=1, 
                          dash="dot",
                         ))
        )
        
        
        figq.add_shape(
        # Line Horizontal
            dict(
                type="line",
                x0=0,
                y0=50,
                x1=100,
                y1=50,
                line=dict(color="black",
                          width=1, 
                          dash="dot",
                         ))
        )
        
        
        figq.add_annotation(
            x=10,
            y=70,
            text="Ideal",
            showarrow=False, 
            opacity=0.3)
        
        figq.add_annotation(
            x=45,
            y=70,
            text="Atypical",
            showarrow=False, 
            opacity=0.3)
        
        figq.add_annotation(
            x=10,
            y=25,
            text="Acceptable",
            showarrow=False, 
            opacity=0.3)
        
        figq.add_annotation(
            x=45,
            y=25,
            text="Negative",
            showarrow=False, 
            opacity=0.3)
        
        figq.update_layout(
            title='<b>Higher Education Institutions by Score Quintiles:</b><br>'+ departamentos,
            title_x=0.5,
            xaxis_title=dict(text='% of Students in Lowest Quintile of Score', font = dict(size=12)),
            yaxis_title=dict(text='% of Students in Highest Quintile of Score', font = dict(size=12)),
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#F9F9F9", 
            showlegend=False, 
            yaxis=dict(range=[-1,101]), 
            xaxis=dict(range=[-1,80]), 
            titlefont= dict(size=14), 
            legend=dict(font=dict(family="sans-serif", size=10, color="black"), x=0.8, y=1)            
            
        )
        
        
        
        
        return figq


#TOAST CALLBACK
@app.callback(
    Output("simple-toast5", "is_open"),
    [Input("simple-toast-toggle5", "n_clicks")],
)
def open_toast2(n):
    if n:
        return True
    return False
