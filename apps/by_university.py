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



from app import app

#Read in data
df = pd.read_csv('pro.csv', low_memory=False)

#Define variables for reactive components
period = df['periodo'].unique()

university_options = df['inst_nombre_institucion'].dropna().unique()

vars1 = ("estu_genero", "estu_areareside", "estu_pagomatriculabeca", "estu_pagomatriculacredito", "estu_pagomatriculapadres",
"estu_pagomatriculapropio", "estu_comocapacitoexamensb11", "fami_hogaractual", "fami_cabezafamilia", "fami_numpersonasacargo",
"fami_educacionpadre", "fami_educacionmadre", "fami_ocupacionpadre", "fami_ocupacionmadre", "fami_estratovivienda", "fami_personashogar",
"fami_cuartoshogar", "fami_tieneinternet", "fami_tienecomputador", "fami_tienelavadora", "fami_tienehornomicroogas", "fami_tienetelevisor",
"fami_tieneautomovil", "fami_tienemotocicleta", "fami_numlibros", "estu_dedicacionlecturadiaria", "estu_dedicacioninternet", "estu_prgm_academico")

vars2 = ("estu_genero", "estu_areareside", "estu_pagomatriculabeca", "estu_pagomatriculacredito", "estu_pagomatriculapadres",
"estu_pagomatriculapropio", "estu_comocapacitoexamensb11", "fami_hogaractual", "fami_cabezafamilia", "fami_numpersonasacargo",
"fami_educacionpadre", "fami_educacionmadre", "fami_ocupacionpadre", "fami_ocupacionmadre", "fami_estratovivienda", "fami_personashogar",
"fami_cuartoshogar", "fami_tieneinternet", "fami_tienecomputador", "fami_tienelavadora", "fami_tienehornomicroogas", "fami_tienetelevisor",
"fami_tieneautomovil", "fami_tienemotocicleta", "fami_numlibros", "estu_dedicacionlecturadiaria", "estu_dedicacioninternet", "estu_prgm_academico")

wrapper = textwrap.TextWrapper(width=11) #Text wrapper so that long academic program labels are wrapped in legend




####STYLES: (this should be in a css file)
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



##################### Layout ######################################


layout = html.Div(
    [
html.Div(
    [
        #SIDEBAR
        
        html.H4("Explore by University", className="display-4", 
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
        
        #University
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
        
        
        #Academic Program
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

         #Var 1
        html.P(
            "Student Variable 1", className="lead"
        ),
        dcc.Dropdown(
        id='var1',
        options=[{'label': i, 'value': i} for i in vars1],
        placeholder="Select a Variable", 
        multi=False,
        className= "mb-4",      
        style={'width': '100%'}
        ), 
        
        
        
        #Var 2
        html.P(
            "Student Variable 2", className="lead"
        ),
        dcc.Dropdown(
        id='var2',
        options=[{'label': i, 'value': i} for i in vars2],
        placeholder="Select a Second Variable", 
        #multi=True,
        style={'width': '100%'}
        ), 
        
        
    ],
    style=SIDEBAR_STYLE,
   
),
        html.Div(
        [

            ########################Row1
            dbc.Row(
            [
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="avg_uni_text"), 
                    
                    html.P(
                    html.Span("Average Score at University", id="tooltip-avg_uni",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Average value of selected score at institution.", target="tooltip-avg_uni", placement="bottom")
                ],
                id="avg_uni", style = mini_container
                                ))),
                
                
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="avg_col_text"), 
                     html.P(
                    html.Span("Average Score Colombia", id="tooltip-avg_col",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Average value of selected score across all institutions in Colombia", target="tooltip-avg_col", placement="bottom")
                ],
                id="avg_col", style = mini_container
                                ))),
                
                
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="avg_dpto_text"), 
                    html.P(
                    html.Span("Average Score Department", id="tooltip-avg_dpto",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Average value of selected score across universities at Department where institution operates", target="tooltip-avg_dpto", placement="bottom")
                ],
                id="avg_dpto", style = mini_container
                                ))),
                
                dbc.Col(html.Div(html.Div(
                [
                    html.H6(id="rank_text"), 
                    html.P(
                    html.Span("Rank", id="tooltip-rank",
                    style={"textDecoration": "underline", "cursor": "pointer"},
                    )) , 
                    
                    dbc.Tooltip("Ranking of the University on the selected score", target='tooltip-rank', placement="bottom")
                ],
                id="rank", style = mini_container
                                ))),
            ],
            
            
        ), 
                    
                    
             ######################################################Row2
            dbc.Row(
            [
                dbc.Col(
                        
                        [dbc.Button(
                            html.Span([html.I(className="fas fa-question-circle ml-0"), ""]), id="simple-toast-toggle", color="#395CA3", outline=False),
                         dbc.Toast(
                             [html.P("This is the content of the toast. This is the content of the toast. This is the content of the toast. This is the content of the toast. This is the content of the toast", className="mb-0")],
                             id="simple-toast",
                             header="This is the header",
                             icon="#395CA3", is_open=False,
                             dismissable=True,
                         ),
                         dcc.Graph(id="score_over_period")],
                            id="score_over_period_Container",
                        
                        style = pretty_container),
                
                
                dbc.Col(html.Div(id="dt_university"
                
                
                    
                )
                    , style = pretty_container),
            ]
        ),
            

            
            #row3
            dbc.Row(
                
                [
            
            dbc.Col(
                        
                        [dcc.Graph(id="bar_program")],
                            id="bar_program_Container",
                        
                        style = pretty_container),
                
                
                dbc.Col(
                
                    [dcc.Loading(dcc.Graph(id="program_quantiles"), color="#395CA3", type="default")],
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
@app.callback(
    Output("avg_uni_text", "children"),
    [
        Input("universities", "value"),
        Input("scores", "value"),
    ],
)
def update_avg_uni_text(universities, scores):
    
    if universities is None or scores is None:
        return []
    
    else:
        dff = df[['inst_nombre_institucion', scores]]
        dff = dff.loc[dff['inst_nombre_institucion'] == universities]
        return dff[scores].mean().round(2)


@app.callback(
    Output("avg_col_text", "children"),
    [
        Input("scores", "value"),
    ],
)


def update_avg_col_text(scores):
    
    if scores is None:
        return []
    
    else:
        return df[scores].mean().round(2)


@app.callback(
    Output("avg_dpto_text", "children"),
    [
        Input("universities", "value"),
        Input("scores", "value"),
    ],
)
def update_avg_dpto_text(universities, scores):
    
    if universities is None or scores is None:
        return []
    
    else:
        dfd = df.loc[df['inst_nombre_institucion'] == universities]
        dpto = dfd['estu_inst_departamento'].unique()
        dfd2 = df.loc[df['estu_inst_departamento'] == dpto[0]]
        return dfd2[scores].mean().round(2)    
    

    
    
@app.callback(
    Output("dt_university", "children"),
    [
        Input("scores", "value"),
    ],
)

def create_data_table(scores):
    if scores is None:
        df_rank = df[['inst_nombre_institucion']]
        df_rank = df_rank.groupby('inst_nombre_institucion').count()
        df_rank['Rank'] = ""
        df_rank['Institution'] = df_rank.index
        df_rank['Score'] = ""
        #df_rank.drop(df_rank.columns[[0]], axis=1, inplace=True)
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
        df_rank = df[[scores, 'inst_nombre_institucion']]
        df_rank = df_rank.groupby('inst_nombre_institucion').mean().sort_values(scores, ascending=False)
        df_rank = df_rank.round({scores: 2})
        df_rank['Rank'] = np.arange(1, len(df_rank)+1)
        df_rank['Institution'] = df_rank.index
        df_rank = df_rank[['Rank','Institution', scores]]
        
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
    
    
@app.callback(
    Output("rank_text", "children"),
    [
        Input("universities", "value"),
        Input("scores", "value"),
    ],
)
    
def update_rank_text(universities, scores):
    if universities is None or scores is None:
        return []
    
    else:
        df_rank = df[[scores, 'inst_nombre_institucion']]
        df_rank = df_rank.groupby('inst_nombre_institucion').mean().sort_values(scores, ascending=False)
        df_rank['Rank'] = np.arange(1, len(df_rank)+1)
        df_rank['Institution'] = df_rank.index
        df_rank = df_rank.loc[df_rank['Institution'] == universities]
        
        return df_rank['Rank']
    

@app.callback(
    Output('program', 'options'),
    [
        Input("universities", "value")
    ],
)

def set_program_options(universities):
    if universities is None:
        return []
    else:
        dfp = df.loc[df['inst_nombre_institucion'] == universities]
        program_options = dfp['estu_prgm_academico'].unique()
        return [{'label': i, 'value': i} for i in program_options]

    
#Line graph
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
        colombia = df[scores].groupby(df['periodo']).mean()
        university = df[scores].loc[df['inst_nombre_institucion'] == universities].groupby(df['periodo']).mean().round(2)
        dbu = df.loc[df['inst_nombre_institucion'] == universities]
        programv = dbu[scores].loc[dbu['estu_prgm_academico'] == program].groupby(df['periodo']).mean().round(2)
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
        colombia = df[scores].groupby(df['periodo']).mean()
        university = df[scores].loc[df['inst_nombre_institucion'] == universities].groupby(df['periodo']).mean().round(2)
        dbu = df.loc[df['inst_nombre_institucion'] == universities]
        programv = dbu[scores].loc[dbu['estu_prgm_academico'] == program].groupby(df['periodo']).mean().round(2)
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
        colombia = df[scores].groupby(df['periodo']).mean()
        university = df[scores].loc[df['inst_nombre_institucion'] == universities].groupby(df['periodo']).mean().round(2)
        dbu = df.loc[df['inst_nombre_institucion'] == universities]
        programv = dbu[scores].loc[dbu['estu_prgm_academico'] == program].groupby(df['periodo']).mean().round(2)
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
    
    
#program_waffle
@app.callback(
    Output('program_quantiles', 'figure'),
    [
        Input("universities", "value"), 
        Input("scores", "value")
    ],
)

def update_program_quantiles(universities, scores):

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
                'text' : '<b>Academic Programs by Score Quantiles:</b><br>' + 'Select Academic Institution and Saber Pro Score'
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }
    
    else:
        dfu = df.loc[df['inst_nombre_institucion'] == universities]
        #dfu['gp'] = dfu[['estu_nucleo_pregrado', 'estu_prgm_academico']].apply(lambda x: '_'.join(x), axis=1)
        dfu['gp'] = dfu['estu_nucleo_pregrado'] + '_' + dfu['estu_prgm_academico']   
        program_mean = pd.DataFrame(dfu[scores].groupby(dfu['gp']).mean())
        program_mean['gp'] = program_mean.index
        program_mean = program_mean.reset_index(drop=True)
        program_mean[['estu_nucleo_pregrado','estu_prgm_academico']] = program_mean.gp.str.split("_",expand=True) 
        grupo_mean = pd.DataFrame(df[scores].groupby(df['estu_nucleo_pregrado']).mean())
        grupo_mean['estu_nucleo_pregrado']=grupo_mean.index
        grupo_mean = grupo_mean.reset_index(drop=True)
        new_df = pd.merge(program_mean, grupo_mean, on='estu_nucleo_pregrado')
        new_df['compare']= np.where(new_df[new_df.columns[0]]>new_df[new_df.columns[4]], 'Above average', 'Below average')
        
        dfb = df.loc[df['inst_nombre_institucion'] == universities]
        dfb['quintile'] = pd.qcut(df[scores], 5, labels=False)
        quintiles = pd.crosstab(dfb.estu_prgm_academico, dfb.quintile).rename_axis(None, axis=1)
        quintiles= pd.DataFrame({
             'quantile_5': round(quintiles[4.0]/(quintiles[0.0]+quintiles[1.0]+quintiles[2.0]+quintiles[3.0]+quintiles[4.0]),4)*100,
             'quantile_1': round(quintiles[0.0]/(quintiles[0.0]+quintiles[1.0]+quintiles[2.0]+quintiles[3.0]+quintiles[4.0]),4)*100
            })
        final_df = pd.merge(quintiles, new_df, on='estu_prgm_academico')
        
        
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(
            x=final_df['quantile_1'].loc[final_df['compare'] == 'Below average'],
            y=final_df['quantile_5'].loc[final_df['compare'] == 'Below average'],
            hovertext=final_df['estu_prgm_academico'].loc[final_df['compare'] == 'Below average'],
            hoverlabel=dict(namelength=0),
            hovertemplate='%{hovertext}<br>1st Quantile: %{x}%  <br>5th Quantile: %{y}% ',
            mode='markers',
            marker_color="#E15759", 
            name="Below average<br>when compared with<br>similar programs in Col"
        ))
        fig2.add_trace(go.Scatter(
            x=final_df['quantile_1'].loc[final_df['compare'] == 'Above average'],
            y=final_df['quantile_5'].loc[final_df['compare'] == 'Above average'],
            hovertext=final_df['estu_prgm_academico'].loc[final_df['compare'] == 'Above average'],
            hoverlabel=dict(namelength=0),
            hovertemplate='%{hovertext}<br>1st Quantile: %{x}% <br>5th Quantile: %{y}% ',
            mode='markers',
            marker_color="#59A14F", 
            name="Above average<br>when compared with<br>similar programs in Col"
        ))
        
        fig2.add_shape(
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
        
        
        fig2.add_shape(
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
        
        
        fig2.add_annotation(
            x=10,
            y=70,
            text="Ideal",
            showarrow=False, 
            opacity=0.3)
        
        fig2.add_annotation(
            x=45,
            y=70,
            text="Atypical",
            showarrow=False, 
            opacity=0.3)
        
        fig2.add_annotation(
            x=10,
            y=25,
            text="Acceptable",
            showarrow=False, 
            opacity=0.3)
        
        fig2.add_annotation(
            x=45,
            y=25,
            text="Negative",
            showarrow=False, 
            opacity=0.3)
        
        fig2.update_layout(
            title='<b>Academic Programs by Score Quantiles:</b><br>'+ universities,
            title_x=0.5,
            xaxis_title=dict(text='% of Students in 1st Quantile of Score', font = dict(size=12)),
            yaxis_title=dict(text='% of Students in 5th Quantile of Score', font = dict(size=12)),
            plot_bgcolor="#F9F9F9",
            paper_bgcolor="#F9F9F9", 
            showlegend=True, 
            yaxis=dict(range=[-1,101]), 
            xaxis=dict(range=[-1,80]), 
            titlefont= dict(size=14), 
            legend=dict(font=dict(family="sans-serif", size=10, color="black"), x=0.8, y=1)            
            
        )
        
        
        
        
        return fig2


#"bar_program"
@app.callback(
    Output('bar_program', 'figure'),
    [
        Input("universities", "value"), 
        Input("scores", "value")
    ],
)

def update_program_boxes(universities, scores):
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
                'text' : '<b>Score Distribution of Academic Programs:</b><br>' + 'Select Academic Institution and Saber Pro Score'
            },
            'titlefont': {
                'size':'14'
            },
            'plot_bgcolor': "#F9F9F9",
            'paper_bgcolor':"#F9F9F9"
        }
               }
    
    else:
        dfn = df[['inst_nombre_institucion', 'estu_prgm_academico', scores]]
        dfn = dfn.loc[dfn['inst_nombre_institucion'] == universities]
        
        program_medians = dfn.groupby('estu_prgm_academico')[scores].median().sort_values(ascending=False) 
        N = len(program_medians.index)     # Number of boxes
        
        #colors
        c = ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]
        
        #Box-plot
        
        fig3 = go.Figure(data=[go.Box(
            y=dfn.loc[dfn['estu_prgm_academico'] == program_medians.index[i],scores],
            marker_color=c[i], 
            name=wrapper.fill(program_medians.index[i]).replace('\n', '<br>')
        ) for i in range(int(N))])
        
        # format the layout
        fig3.update_layout(
            title='<b>Score Distribution of Academic Programs:</b><br>'+ universities,
            title_x=0.5,
            titlefont= dict(size=14), 
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(zeroline=False, gridcolor='#E9E9E9'),
            hovermode="x unified",
            paper_bgcolor='#F9F9F9',
            plot_bgcolor='#F9F9F9',
            legend=dict(font=dict(family="sans-serif", size=8, color="black")) 
        )
        
        return fig3


    
@app.callback(
    Output("simple-toast", "is_open"),
    [Input("simple-toast-toggle", "n_clicks")],
)
def open_toast(n):
    if n:
        return True
    return False

    
    
    
#explore_vars_graph
