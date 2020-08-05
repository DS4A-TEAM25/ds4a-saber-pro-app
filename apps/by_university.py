import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import textwrap #
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_table as dt
import numpy as np
from utils import *
from textwrap import dedent
from sqlalchemy import create_engine

from app import app


#Define variables for reactive components

#University options
university_options = get_unique(engine, 'pro_data', 'inst_nombre_institucion')
university_options = list(filter(lambda a: a != None , university_options))
university_options = sorted(university_options)

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
        #SIDEBAR MENU
        
        html.H4("Explore by University", className="display-4", 
                   style = {'font-size': '36px'}),
        html.Hr(),
        
        #Period Slider
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
        
        #University Dropdown
        html.P(
            "Academic Institution", className="lead"
        ),
        dcc.Dropdown(
        id='universities',
        options=[{'label': i, 'value': i} for i in university_options],
        placeholder="Search for an Institution",  
        multi=False,
        className= "mb-4",    
        optionHeight=80,
        style={'width': '100%'}
        ), 
        
        
        #Score Dropdown
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
        
        
        #Academic Program Dropdown
        html.P(
            "Academic Program", className="lead"
        ),
        dcc.Dropdown(
        id='program',     
        placeholder="Select a Program",
        multi=False,
        className= "mb-4",
        optionHeight=80,    
        style={'width': '100%'}
        ), 

         #Student Variable 1 Dropdown
        html.P(
            "Student Variables", className="lead"
        ),
        dcc.Dropdown(
        id='var1',
         options=[
            {'label': 'Gender', 'value': 'estu_genero'},
            {'label': 'Mothers Education Level' , 'value': 'fami_educacionmadre'},
            {'label': 'DANE Estrato', 'value': 'fami_estratovivienda'},
            {'label': 'Internet Access', 'value': 'fami_tieneinternet'},
            {'label': 'Number of books in household', 'value': 'fami_numlibros'},
            {'label': 'Hours spent Reading', 'value': 'estu_dedicacionlecturadiaria'},
            {'label': 'Tuition paid with loan', 'value': 'estu_pagomatriculacredito'}, 
            {'label': 'Tuituion paid by parents', 'value': 'estu_pagomatriculapadres'},
            {'label': 'SABER PRO preparation', 'value': 'estu_comocapacitoexamensb11'},  
        ],
        placeholder="Select a Variable", 
        multi=False,
        className= "mb-4",      
        style={'width': '100%'}
        ), 
      
    ],
    style=SIDEBAR_STYLE,
   
),
        
        #OUTPUT LAYOUT
        html.Div(
        [

            ########################Row1
            dbc.Row(
            [
                #Average Score University card
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="avg_uni_text"), 
                    
                    html.P(
                    html.Span("Average Score at University", id="tooltip-avg_uni",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Average score of selected skill at institution.", target="tooltip-avg_uni", placement="bottom")
                ],
                id="avg_uni", style = mini_container
                                ))),
                
                 #Average Score Colombia card
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="avg_col_text"), 
                     html.P(
                    html.Span("Average Score Colombia", id="tooltip-avg_col",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Average score of selected skill across all institutions in Colombia", target="tooltip-avg_col", placement="bottom")
                ],
                id="avg_col", style = mini_container
                                ))),
                
                #Average Score Department card
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="avg_dpto_text"), 
                    html.P(
                    html.Span("Average Score Department", id="tooltip-avg_dpto",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Average score of selected skill across all universities within the Department where the institution operates", target="tooltip-avg_dpto", placement="bottom")
                ],
                id="avg_dpto", style = mini_container
                                ))),
                
                #Rank card
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="rank_text"), 
                    html.P(
                    html.Span("Rank", id="tooltip-rank",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Ranking of institution on the selected skill out of all institutions in Colombia", target='tooltip-rank', placement="bottom")
                ],
                id="rank", style = mini_container
                                ))),
            ],
            
            
        ), 
                    
                    
             ######################################################Row2
            dbc.Row(
            [
                #Line Graph Container
                dbc.Col(
                        
                        [
                            dbc.Button(
                            html.Span([html.I(className="fas fa-question-circle ml-0"), ""]), id="simple-toast-toggle", color="#395CA3", outline=False),
                         dbc.Toast(
                             [html.P("This graph shows the average score of the selected higher education institution, the average score of the selected academic program and Colombia's average score over time.", className="mb-0")],
                             id="simple-toast",
                             header="Saber Pro Score Over Time",
                             icon="#395CA3", is_open=False,
                             dismissable=True,
                         ),
                         dcc.Graph(id="score_over_period")
                        ],
                            id="score_over_period_Container",
                        
                        style = pretty_container),
                
                #Table with Rankings Container
                dbc.Col(
                    [
                        dbc.Button(
                            html.Span([html.I(className="fas fa-question-circle ml-0"), ""]), id="simple-toast-toggle2", color="#395CA3", outline=False),
                         dbc.Toast(
                             [html.P("This table shows the ranking of universities by the selected score. You can sort and filter the table (filter is case sensitive). ", className="mb-0")],
                             id="simple-toast2",
                             header="University Score Ranking",
                             icon="#395CA3", is_open=False,
                             dismissable=True,
                         ),
                        html.Div(id="dt_university")
                    ]
                    , style = pretty_container),
            ]
        ),
            

            
            #row3
            dbc.Row(
                
                [
            
            #Boxplot Container        
            dbc.Col(
                        
                        [
                            dbc.Button(
                            html.Span([html.I(className="fas fa-question-circle ml-0"), ""]), id="simple-toast-toggle3", color="#395CA3", outline=False),
                         dbc.Toast(
                             [html.P("This graph shows a bar plot, for the selected academic program of the selected univeristy, that describes the average selected score by student characteristic.", className="mb-0")],
                             id="simple-toast3",
                             header="Bar Plot of Academic Program by Student Variable",
                             icon="#395CA3", is_open=False,
                             dismissable=True,
                         ),
                            dcc.Graph(id="bar_program")
                        ],
                            id="bar_program_Container",
                        
                        style = pretty_container),
                
            #Quintile Plot Container     
                dbc.Col(
                
                    [
                        dbc.Button(
                            html.Span([html.I(className="fas fa-question-circle ml-0"), ""]), id="simple-toast-toggle4", color="#395CA3", outline=False),
                         dbc.Toast(
                             [html.P("The population of all Colombian students was divided into 5 groups, according to their score on the selected skill. Students that scored on the highest quintile of the distribution had the best performance, while students that score on the lowest quintile had the worst. This graph plots academic programs at the selected university based on these score quintiles. Each observation represents an academic program within the selected university. The x-axis shows the percentage of students that scored on the lowest quintile (1st quintile). The y-axis shows the percentage of students that scored on the highest quintile(5th quintile). Ideally you want to have most of your students scoring in the 5th quintile, and very few scoring in the 1st. The academic programs are also compared to similiar programs in Colombia based on the NBC(NUCLEO DE CONOCIMIENTOS BASICOS) classification created by Mineducacion. For example, all engineering programs are classified under the engineering category. Academic programs in red scored lower than average relative to programs in the same NBC group. Academic programs in green scored higher than average when compared to other programs in the same NBC group.", className="mb-0")],
                             id="simple-toast4",
                             header="Quintile Plot of Academic Programs",
                             icon="danger", is_open=False,
                             dismissable=True,
                         ),
                        
                        dcc.Loading(dcc.Graph(id="program_quantiles"), color="#395CA3", type="default")],
                            id="program_quantiles_Container",
                        
                        style = pretty_container),
                
            ]
                
                
                )
            
            
            
           
            
            
            
        
            
        ], 
            style= CONTENT_STYLE
        
        
        ) 
        
         
        
        
    ]
)




##################### Callbacks ######################################


###RETURN ACADEMIC PROGRAMS IN DROPDOWN AFTER UNIVERSITY SELECTION  
@app.callback(
    Output('program', 'options'),
    [
        Input("universities", "value"), 
        Input("period_slider", "value")
    ],
)

def set_program_options(universities, period_slider):
    if universities is None:
        return []
    else:
        p=[str(period_slider[0]), str(period_slider[1])] 
        program_options = get_unique_conditional(engine, "pro_data", "estu_prgm_academico", "inst_nombre_institucion", "'"+str(universities)+"'", "'"+p[0]+"'", "'"+p[1]+"'")
        program_options = list(filter(lambda a: a != None , program_options))
        program_options  = sorted(program_options)
        return [{'label': i, 'value': i} for i in program_options]
    
    

#TOAST CALLBACKS THAT APPEAR WHEN YOU CLICK ON THE HELP BUTTON ON EACH GRAPH   
    
@app.callback(
    Output("simple-toast", "is_open"),
    [Input("simple-toast-toggle", "n_clicks")],
)
def open_toast(n):
    if n:
        return True
    return False


@app.callback(
    Output("simple-toast2", "is_open"),
    [Input("simple-toast-toggle2", "n_clicks")],
)
def open_toast2(n):
    if n:
        return True
    return False

@app.callback(
    Output("simple-toast3", "is_open"),
    [Input("simple-toast-toggle3", "n_clicks")],
)
def open_toast2(n):
    if n:
        return True
    return False

@app.callback(
    Output("simple-toast4", "is_open"),
    [Input("simple-toast-toggle4", "n_clicks")],
)
def open_toast2(n):
    if n:
        return True
    return False


### AVERAGE SCORE OF UNIVERSITY CARD    
@app.callback(
    Output("avg_uni_text", "children"),
    [
        Input("scores", "value"),
        Input("period_slider", "value"), 
         Input("universities", "value")
    ],
)


def update_avg_dpt(scores, period_slider, universities):
    
    if universities is None or scores is None:
        return []
    
    else:
        

        p=[str(period_slider[0]), str(period_slider[1])] 
        mean_uni = get_avg(engine, 'pro_data', scores, "inst_nombre_institucion", "'"+str(universities)+"'", "'"+p[0]+"'", "'"+p[1]+"'")
        if mean_uni[0]!= None:
            return round(mean_uni[0],2)
        else: 
            return str("No Data for Selected Period")
    

#AVERAGE OF DEPARTMENT TEXT
@app.callback(
    Output("avg_dpto_text", "children"),
    [
        Input("universities", "value"),
        Input("scores", "value"),
         Input("period_slider", "value"), 
    ],
)
def update_avg_dpto_text(universities, scores, period_slider):
    
    if universities is None or scores is None:
        return []
    
    else:
        
        p=[str(period_slider[0]), str(period_slider[1])] 
        dpto_uni = get_avg_input3(engine, 'pro_data', scores, "estu_inst_departamento", "inst_nombre_institucion", "'"+str(universities)+"'", "'"+p[0]+"'", "'"+p[1]+"'")
        if len(dpto_uni)!= 0:
            return str(round(dpto_uni[0][1],2)) + " (" + str(dpto_uni[0][0]) + ")"
        else: 
            return str("No Data for Selected Period")
    
    
    
### RANK
@app.callback(
    Output("rank_text", "children"),
    [
        Input("scores", "value"),
        Input("period_slider", "value"), 
         Input("universities", "value")
    ],
)


def update_rank2(scores, period_slider, universities):
    
    if universities is None or scores is None:
        return []
    
    else:
        
        p=[str(period_slider[0]), str(period_slider[1])] 
        mean_score = pd.read_sql("SELECT inst_nombre_institucion,AVG("+scores+") mean_score FROM pro_data WHERE periodo BETWEEN '"+p[0]+ "' AND '" +p[1]+"'  GROUP BY inst_nombre_institucion", engine.connect())
        if len(mean_score[mean_score.inst_nombre_institucion==universities])!= 0:
            mean_score  = mean_score .dropna()
            total_universities = str(len(mean_score['inst_nombre_institucion'].unique()))
            mean_score = mean_score.sort_values(by='mean_score', ascending=False).reset_index(drop=True)
            mean_score.index = mean_score.index + 1
            return str(mean_score.index[mean_score.inst_nombre_institucion==universities][0]) + "/" + total_universities 
        else: 
            return str("No Data for Selected Period")
    
    

    
    
###CREATE DATA TABLE

@app.callback(
    Output("dt_university", "children"),
    [
        Input("scores", "value"),
        Input("period_slider", "value"), 
    ],
)


def create_data_table(scores, period_slider):
    if scores is None:
        scores = "mod_razona_cuantitat_punt"
        df_rank = pd.read_sql("SELECT inst_nombre_institucion,AVG("+scores+") mean_score FROM pro_data GROUP BY inst_nombre_institucion", engine.connect())
        df_rank =df_rank.dropna()
        df_rank['Rank'] = ""
        df_rank['Institution'] = df_rank['inst_nombre_institucion']
        df_rank['Score'] = ""
        df_rank.drop(df_rank.columns[[0,1]], axis=1, inplace=True)
        
        dt_empty = dt.DataTable(
                    data=df_rank.to_dict('records'), id="table1",
                    columns=[{"name": i, "id": i} for i in df_rank.columns],
                    sort_action="native",
                    sort_mode="multi", 
                    page_size=10,
                    style_header={'backgroundColor': '#395CA3', 'color':'white'},
                    style_cell={
                        'whiteSpace': 'normal',
                        'height': 'auto', 
                        'textAlign': 'left'
    }
                )

        return dt_empty
    
    else:
        p=[str(period_slider[0]), str(period_slider[1])] 
        df_rank = pd.read_sql("SELECT inst_nombre_institucion,AVG("+scores+") mean_score FROM pro_data WHERE periodo BETWEEN '"+p[0]+ "' AND '" +p[1]+"'  GROUP BY inst_nombre_institucion", engine.connect())
        df_rank = df_rank.sort_values(by='mean_score', ascending=False).reset_index(drop=True)
        df_rank = df_rank.dropna()
        df_rank.index = df_rank.index + 1
        df_rank['Rank'] = df_rank.index
        df_rank['Institution'] = df_rank['inst_nombre_institucion']
        df_rank['Score'] = round(df_rank['mean_score'], 2)
        df_rank.drop(df_rank.columns[[0,1]], axis=1, inplace=True)
        
        dt_university= dt.DataTable(
                    data=df_rank.to_dict('records'), id="table1",
                    columns=[{"name": i, "id": i} for i in df_rank.columns],
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi", 
                    page_size=10,
                    style_header={'backgroundColor': '#395CA3', 'color':'white'},
                    style_cell={
                        'whiteSpace': 'normal',
                        'height': 'auto', 
                        'textAlign': 'left'
    }
                )
        
        return dt_university
    
    
### CREATE LINE GRAPH
@app.callback(Output("score_over_period", "figure"), [Input("scores", "value"), 
                                                     Input("universities", "value"), 
                                                     Input("program", "value")])

def make_line_graph(scores, universities, program):
    
    if scores is None:
        return {"layout": {
            "xaxis": {
                "visible": True, 
                'range': [2016,2019], 
                'dtick' : 1
            },
            "yaxis": {
                "visible": True, 
                'range':[0,300]
            },
            'title': {
                'text' : '<b>Average Score over time:</b><br>' + 'Select Academic Institution and Saber Pro Score'
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }        
    
    
    if universities is None:
        colombia = pd.read_sql("SELECT periodo,AVG("+scores+") mean_score FROM pro_data  GROUP BY periodo", engine.connect())
        period = colombia['periodo']
        colombia = colombia['mean_score'].round(2)
        data = [
            dict(
                type="scatter",
                mode="lines+markers",
                name="Colombia",
                x=period,
                y=colombia,
                line=dict(shape="spline", smoothing="1", color="#F9ADA0"),
            ),
        ]
        layout_graph = dict(
            hovermode="closest",
            title= dict(text = '<b>Average Score over time</b><br>' + "Colombia"), 
            titlefont= dict(size=14), 
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#F9F9F9")
        figure = dict(data=data, layout=layout_graph)
        return figure
    
    if program is None:
        colombia = pd.read_sql("SELECT periodo,AVG("+scores+") mean_score FROM pro_data  GROUP BY periodo", engine.connect())
        period = colombia['periodo']
        colombia = colombia['mean_score'].round(2)
        university = pd.read_sql("SELECT periodo,AVG("+scores+") mean_score FROM pro_data WHERE inst_nombre_institucion = '"+universities+"' GROUP BY periodo", engine.connect())
        university = university['mean_score'].round(2)
        data = [
            dict(
                type="scatter",
                mode="lines+markers",
                name="Colombia",
                x=period,
                y=colombia,
                line=dict(shape="spline", smoothing="1", color="#F9ADA0"),
            ),
            
            dict(
                type="scatter",
                mode="lines+markers",
                name="University",
                x=period,
                y=university,
                line=dict(shape="spline", smoothing="1", color="#849E68"),
            ),
        ]
        layout_graph = dict(
            hovermode="closest",
            title= dict(text = '<b>Average Score over time:</b><br>' + universities), 
            titlefont= dict(size=14), 
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#F9F9F9")
        figure = dict(data=data, layout=layout_graph)
        return figure
    
    else:
        colombia = pd.read_sql("SELECT periodo,AVG("+scores+") mean_score FROM pro_data  GROUP BY periodo", engine.connect())
        period = colombia['periodo']
        colombia = colombia['mean_score'].round(2)
        university = pd.read_sql("SELECT periodo,AVG("+scores+") mean_score FROM pro_data WHERE inst_nombre_institucion = '"+universities+"' GROUP BY periodo", engine.connect())
        university = university['mean_score'].round(2)
        programv = pd.read_sql("SELECT periodo,AVG("+scores+") mean_score FROM pro_data WHERE estu_prgm_academico = '"+program+"' GROUP BY periodo", engine.connect())
        programv = programv['mean_score'].round(2)
        data = [
            dict(
                type="scatter",
                mode="lines+markers",
                name="Colombia",
                x=period,
                y=colombia,
                line=dict(shape="spline", smoothing="1", color="#F9ADA0"),
            ),
            dict(
                type="scatter",
                mode="lines+markers",
                name="University",
                x=period,
                y=university,
                line=dict(shape="spline", smoothing="1", color="#849E68"),
            ),
            dict(
                type="scatter",
                mode="lines+markers",
                name="Program",
                x=period,
                y=programv,
                line=dict(shape="spline", smoothing="1", color="#59C3C3"),
            ),
        ]
        layout_graph = dict(
            hovermode="closest",
            title= dict(text = '<b>Average Score over time:</b><br>' + universities), 
            titlefont= dict(size=14), 
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#F9F9F9")
        figure = dict(data=data, layout=layout_graph)
        return figure

### CREATE QUINTILE PLOT
@app.callback(
    Output('program_quantiles', 'figure'),
    [
        Input("universities", "value"),
        Input("period_slider", "value"), 
        Input("scores", "value")
    ],
)

def update_program_quantiles(universities, period_slider, scores):

    if universities is None or scores is None:
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
                'text' : '<b>Academic Programs by Score Quintiles:</b><br>' + 'Select Academic Institution and Saber Pro Score'
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
        
        #Quintile df
        quint_table = get_pct(engine, "pro_data", "estu_prgm_academico", quintile_score, scores,"inst_nombre_institucion", "'"+str(universities)+"'", "'"+p[0]+"'", "'"+p[1]+"'") 
        quint_table = pd.DataFrame(quint_table, columns = ['estu_prgm_academico', 'sum_quintil_1', 'sum_quintil_5', 'sum_students', 'avg_score'])
        quint_table['pct_quint1'] = round(quint_table['sum_quintil_1']/quint_table['sum_students'] * 100,2)
        quint_table['pct_quint5'] =round(quint_table['sum_quintil_5']/quint_table['sum_students'] * 100,2)
        
        #School averages df
        average_program = pd.read_sql("SELECT estu_nucleo_pregrado,AVG("+scores+") mean_score_school FROM pro_data  WHERE inst_nombre_institucion = '"+universities+"'  GROUP BY estu_nucleo_pregrado", engine.connect())
        programs = pd.read_sql("SELECT DISTINCT estu_prgm_academico FROM pro_data  WHERE inst_nombre_institucion = '"+universities+"'", engine.connect())
        program_key =  pd.read_sql("SELECT * FROM program_key", engine.connect())
        program_key.columns = ['estu_nucleo_pregrado', 'estu_prgm_academico']
        programs = programs['estu_prgm_academico'].tolist()
        program_key = program_key[program_key['estu_prgm_academico'].isin(programs)]
        join_df = pd.merge(average_program, program_key, on='estu_nucleo_pregrado')
                               
        #Combine datasets and create below and above average column
        quint_table = pd.merge(quint_table, join_df, on='estu_prgm_academico')
        quint_table = quint_table.dropna()
        quint_table['compare']= np.where(quint_table[quint_table.columns[4]]>quint_table[quint_table.columns[8]], 'Above average', 'Below average')

        figq = go.Figure()
        figq.add_trace(go.Scatter(
            x=quint_table['pct_quint1'].loc[quint_table['compare'] == 'Below average'] ,
            y=quint_table['pct_quint5'].loc[quint_table['compare'] == 'Below average'] ,
            hovertext=quint_table['estu_prgm_academico'].loc[quint_table['compare'] == 'Below average'] , 
            hoverlabel=dict(namelength=0),
            hovertemplate='%{hovertext}<br>1st Quintile: %{x}%  <br>5th Quintile: %{y}% ',
            mode='markers',
            marker_color="#E15759", 
            name="Below average<br>when compared with<br>similar programs in Col"
        ))
        
        figq.add_trace(go.Scatter(
            x=quint_table['pct_quint1'].loc[quint_table['compare'] == 'Above average'],
            y=quint_table['pct_quint5'].loc[quint_table['compare'] == 'Above average'],
            hovertext=quint_table['estu_prgm_academico'].loc[quint_table['compare'] == 'Above average'], 
            hoverlabel=dict(namelength=0),
            hovertemplate='%{hovertext}<br>1st Quintile: %{x}%  <br>5th Quintile: %{y}% ',
            mode='markers',
            marker_color="#59A14F", 
            name="Above average<br>when compared with<br>similar programs in Col"
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
            title='<b>Academic Programs by Score Quintiles:</b><br>'+ universities,
            title_x=0.5,
            xaxis_title=dict(text='% of Students in Lowest Quintile of Score', font = dict(size=12)),
            yaxis_title=dict(text='% of Students in Highest Quintile of Score', font = dict(size=12)),
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#F9F9F9", 
            showlegend=True, 
            yaxis=dict(range=[-1,101]), 
            xaxis=dict(range=[-1,80]), 
            titlefont= dict(size=14), 
            legend=dict(font=dict(family="sans-serif", size=10, color="black"), x=0.8, y=1)            
            
        )
        
        
        
        
        return figq
    
### CREATE BAR CHART
@app.callback(
    Output('bar_program', 'figure'),
    [
        Input("universities", "value"),
        Input("period_slider", "value"), 
        Input("scores", "value"), 
        Input("var1", "value"), 
        Input("program", "value"),
        
    ],
)

def update_program_bar(universities, period_slider, scores, var1, program):
 
    if universities is None:
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
                'text' : '<b>Average Score by Student Characteristics at Program :</b><br>' + 'Select University, Program and Student Characteristic'
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }
    
    
    if scores is None:
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
                'text' : '<b>Average Score by Student Characteristics at Program :</b><br>' + 'Select University, Program and Student Characteristic'
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }
    
    if  program is None:
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
                'text' : '<b>Average Score by Student Characteristics at Program :</b><br>' + 'Select University, Program and Student Characteristic'
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }
    
    if  var1 is None:
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
                'text' : '<b>Average Score by Student Characteristics at Program :</b><br>' + 'Select University, Program and Student Characteristic'
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
        mean_score = get_avg_multi(engine, "pro_data", scores, var1 , "inst_nombre_institucion", "'"+str(universities)+"'", "estu_prgm_academico", "'"+str(program)+"'", "'"+p[0]+"'", "'"+p[1]+"'")
        mean_score = pd.DataFrame(mean_score, columns = ['variable', 'avg'])
        mean_score = mean_score.dropna()
        mean_score["avg"] = mean_score["avg"].round(2)
        mean_score= mean_score.sort_values(by=['avg'], ascending=False)
        
        figbar = px.bar(mean_score, x='variable', y='avg', color='avg')
        
        # format the layout
        figbar.update_layout(
            title='<b>Average Score by Student Characteristics:</b><br>'+ universities,
            title_x=0.5,
            titlefont= dict(size=14), 
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=True),
            yaxis=dict(zeroline=False, gridcolor='#E9E9E9'),
            hovermode="x unified",
            paper_bgcolor='#F9F9F9',
            plot_bgcolor='#F9F9F9',
            legend=dict(font=dict(family="sans-serif", size=8, color="black")) 
        )
        
        return figbar

    
    
    
    
    
