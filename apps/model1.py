import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
import dash_html_components as html
import pandas as pd
import numpy as np
import os
import glob
#import sklearn.metrics       as Metrics
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor 
import joblib
#from sklearn.model_selection import train_test_split
import pickle
from sqlalchemy import create_engine
from utils import *
from dash.dependencies import Input, Output
from app import app
from math import radians, cos, sin, asin, sqrt
from sqlalchemy import create_engine


#Define variables for reactive components
#Departamento options
departamento_model = get_unique(engine, 'pro_data', "estu_inst_departamento")
departamento_model = sorted(departamento_model)
departamento_model = [x for x in departamento_model if str(x) != 'nan']

#Program Options
prograns_model = get_unique(engine, 'score_programas', "program")
#University Options
university_model = get_unique(engine, 'pro_data', "inst_nombre_institucion")
university_model = list(filter(lambda a: a != None , university_model))
university_model = sorted(university_model)


#ModelQRPrueba = joblib.load('ModelQR.pkl')
#QR1=np.round(ModelQRPrueba.predict([[59, 59, 59, 22, 6, 0,1,1,1,1,0,1,0,0,0,0,0,0]]),0)
#QR1
#X1=int(QR1[0])
#X1


#SIDEBAR DROPDOWNS

############################################################# POSITION ENGLISH
posenglish_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Position Saber 11", className="mr-2"),
                dbc.Input(id="m01", type="number", placeholder="Saber 11 position (0-1000)", min=0, max=1000, step=1),
            ],
            className="mr-3",
        )

    ],
)



########################################################################## SABER 11 MATH SCORE
scoreMathHighSchool_form = dbc.Form(
    [
dbc.FormGroup(
    [
        dbc.Label("Math Score Saber 11", className="mr-2"),
        dbc.Input(id="m03", type="number", placeholder="Saber 11 Math Score (0-150)", min=0, max=150, step=0.01),
    ],
    className="mr-3",
)
    ],
)

############################################################################## SABER 11 ENGLISH SCORE

ScoreEnglishHighSchool_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("English Score Saber 11", className="mr-2"),
                dbc.Input(id="m05", type="number", placeholder="Saber 11 English Score (0-150)", min=0, max=150, step=0.01),
            ],
            className="mr-3",
        )

    ],
)



###########****###################################################################### AGE

age_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Age", className="mr-2"),
                dbc.Input(id="m07", type="number", placeholder="e.g. 23", min=0, max=60, step=1),
            ],
            className="mr-3",
        )

    ],
)


########################################################################################## GENDER

gender_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Gender", className="mr-2"),
                dbc.Select(
                    id="m010",  
                    options=[
                                {"label": "Male", "value": "M"},
                                {"label": "Female", "value": "F"},
                        ],
                )



            ],
            className="mr-3",
        )

    ],
)



#################################################################################### SABER 11 YEAR TAKEN

years11_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber11 was taken", className="mr-2"),
                dbc.Input(id="m09", type="number", placeholder="e.g. 2018", min=1990, max=2019, step=1),
            ],
            className="mr-3",
        )

    ],
)

########################################################################################## SABER PRO YEAR TAKEN

year_pro_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber Pro will be taken", className="mr-2"),
                dbc.Input(id="m011", type="number", placeholder="e.g. 2022", min=2016, max=2025, step=1),
            ],
            className="mr-3",
        )

    ],
)


############################################################################ DEPARTMENT OF RESIDENCE

state_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Department of Residence", className="mr-2"),
                dcc.Dropdown(
                    id="m06",
                    options=[{'label': i, 'value': i} for i in departamento_model],
                    placeholder="Select a Department",
                )
        ],
            className="mr-3",
        )

    ],
)


################################################################################## DEPARTMENT HIGHER INSTITUTION

state_uni_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Department where University is located", className="mr-2"),
                dcc.Dropdown(
                    id="m08",
                    options=[{'label': i, 'value': i} for i in departamento_model], 
                    placeholder="Select a Department",
                )
            ],
            className="mr-3",
        )

    ],
)



############################################################################ UNIVERSITY
university_form = dbc.Form(
    [
        dbc.FormGroup(
            [
    dbc.Label("University", className="mr-2"),
    dcc.Dropdown(
                    id="m04",
                    options=[{'label': i, 'value': i} for i in university_model],
                    placeholder="Select a University",
                    optionHeight=80,
                )
            ],
            className="mr-3",
        )
    ],
)

################################################################### ACADEMIC PROGRAM
program_form = dbc.Form(
    [

    dbc.FormGroup(
        [
            dbc.Label("Academic Program", className="mr-2"),
            dcc.Dropdown(
                    id="m02",
                    placeholder="Select a University and then an Academic Program",
                    optionHeight=80,
                )
        ],
        className="mr-3",
    )
    ],
)

####Callback to get academic program after University Selection
###RETURN ACADEMIC PROGRAMS IN DROPDOWN AFTER UNIVERSITY SELECTION  
@app.callback(
    Output('m02', 'options'),
    [
        Input("m04", "value")
    ],
)

def set_program_options(universities):
    if universities is None:
        return []
    else:
        program_options = get_unique_conditional(engine, "pro_data", "estu_prgm_academico", "inst_nombre_institucion", "'"+str(universities)+"'", "'2016'", "'2019'")
        program_options = list(filter(lambda a: a != None , program_options))
        program_options  = sorted(program_options)
        return [{'label': i, 'value': i} for i in program_options]



########################################################################################### MOTHER'S EDUCATION
mother_level_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Mother's education level", className="mr-2"),
                dbc.Select(
                    id="m012",
                    options=[
                                {"label": "No bachiller", "value": "1"},
                                {"label": "Bachiller", "value": "2"},
                                {"label": "Tecnico", "value": "3"},
                                {"label": "Profesional", "value": "4"},
                                {"label": "Postgrado", "value": "5"},
                                {"label": "NS-NR", "value": "6"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)


######################################################################################################## TUITION COST

value_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Tuition cost range per semester", className="mr-2"),
                dbc.Select(
                    id="m013", 
                    options=[
                                {"label": "Less than  500 thousand", "value": "1"},
                                {"label": "0.5M-4M", "value": "2"},
                                {"label": "4M-7M", "value": "3"},
                                {"label": "7M+", "value": "4"},
                                {"label": "Didn't pay tuition", "value": "5"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)

######################################################################################################## TUITION WHO PAID

credit_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Was a loan used to pay for tuition?", className="mr-2"),
                dbc.Select(
                    id="m014", 
                    options=[
                                {"label": "YES", "value": "YES"},
                                {"label": "NO", "value": "NO"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)



################################################################################################################ TUITION PAYMENTE METHOD
help_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Who paid for tuition?", className="mr-2"),
                dbc.Select(
                    id="m015", 
                    options=[
                                {"label": "Parents", "value": "Parents"},
                                {"label": "Scholarship", "value": "Scholarship"},
                                {"label": "Student", "value": "Myself"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)
################################################################## WISH ME LUCK BUTTON 

suerte_botton = dbc.Button("Wish me luck!", color="primary", id="m016",)



##################################################################



################ LAYOUT OF SIDEBAR MENU
##################################################################################################################
##################################################################################################################

SIDEBAR_STYLE2 = {
    'border-radius': '5px',
    'background-color': '#f9f9f9',
    'margin': '20px',
    'padding': '15px',
    'position': 'relative',
    'box-shadow': '2px 2px 2px lightgrey'
}


tarjeta1 = [
            posenglish_form,
            scoreMathHighSchool_form,
            ScoreEnglishHighSchool_form,
            years11_form,
            year_pro_form,
            age_form,
            gender_form,
            mother_level_form,
]

tarjeta2 =  [
            state_form,
            state_uni_form,
            university_form,
            program_form,
            value_form,
            help_form,
            credit_form,
            suerte_botton,
            
        ]



row_1 = dbc.Row(
    [
        dbc.Col(tarjeta1),
        dbc.Col(tarjeta2),
    ],
    style=SIDEBAR_STYLE2,
)


forumulario = html.Div([row_1])




###############################REACTIVE CARDS WHERE VALUE OF PREDICTION FROM THE MODEL WILL BE DISPLAYED  
#######################################################################################
#######################################################################################


#Container styles
mini_container2 = {
  'border-radius': '5px',
  'background-color': '#FFFFFF',
  'margin': '10px',
  'padding': '15px',
  'position': 'relative',
  'box-shadow': '2px 2px 2px lightgrey'
}



###CONTENT CARD BOXES
card_content_1 = [
    dbc.CardBody(
        [
            html.H3("Quantitative Reasoning", className="card-title"), 
            html.P(
                "Expected Score:",
                className="card-text",
            ),
            html.H3(id="mout_01", style={"vertical-align": "middle"}),

        ]
   ), 
]

card_content_2 = [
    dbc.CardBody(
        [
            html.H3("Citizenship Competence", className="card-title"),          
            html.P(
                "Expected Score:",
                className="card-text",
            ),
            html.H3(id="mout_06", style={"vertical-align": "middle"}),
        ]
    ),
]

card_content_3 = [
    dbc.CardBody(
        [
            html.H3("Critical Reading", className="card-title"), 
            html.P(
                "Expected Score:",
                className="card-text",
            ),
            html.H3(id="mout_02", style={"vertical-align": "middle"}),

        ]
    ),
]

card_content_4 = [
    dbc.CardBody(
        [
            html.H3("English", className="card-title"),             
            html.P(
                "Expected Score:",
                className="card-text",
            ),
            html.H3(id="mout_03", style={"vertical-align": "middle"}),
        ]
    ),
]


card_content_5 = [
    dbc.CardBody(
        [
            html.H3("Writing", className="card-title"),                       
            html.P(
                "Expected Score::",
                className="card-text",
            ),
            html.H3(id="mout_04", style={"vertical-align": "middle"}),
        ]
    ),
]

card_content_6 = [
    dbc.CardBody(
        [
            html.H3("Global Score", className="card-title"),                       
            html.P(
                "Expected Score:",
                className="card-text",
            ),
            html.H3(id="mout_05", style={"vertical-align": "middle"}),
        ]
    ),
]



#### CONTENT LAYOUT

row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_1, color="secondary", outline=True,style = mini_container2)),
        dbc.Col(dbc.Card(card_content_2, color="secondary", outline=True,style = mini_container2)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_3, color="secondary", outline=True,style = mini_container2)),
        dbc.Col(dbc.Card(card_content_4, color="secondary", outline=True,style = mini_container2)),
    ],
    className="mb-4",
)

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_5, color="secondary", outline=True,style = mini_container2)),
        dbc.Col(dbc.Card(card_content_6, color="secondary", outline=True,style = mini_container2)),
    ],
    className="mb-4",
)

cards = html.Div([row_1, row_2, row_3])

esquema = dbc.Row(
    [
        dbc.Col(forumulario),
        dbc.Col(cards),

    ],
    no_gutters=True,
)



button = html.Div(
    [
        dbc.Button("Click me", id="example-button", className="mr-2"),
        html.Span(id="example-output", style={"vertical-align": "middle"}),
    ]
)


layout = html.Div([
    html.H1("Predicting Saber Pro Scores", style = {'color': '4d4d4d', 
                                    'text-shadow': '2px 8px 6px rgba(0,0,0,0.2), 0px -5px 35px rgba(255,255,255,0.3)'}),
    esquema,
])



############################################ MODEL CALLBACKS

@app.callback(Output("mout_01", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m02", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value"),
                                               Input("m06", "value"),
                                               Input("m08", "value")])

                
                
def modelos1(n_clicks, m01,m02, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010,m06,m08):
    if n_clicks is None:
        return ""

    else:

        #############################################################################################################################################
        scrores_3years = pd.read_sql("select CitizenScore3yearsProgram, EnglishScore3yearsProgram,ReadingScore3yearsProgram,QuantitativeReasoningScore3yearsProgram,ComunicationScore3yearsProgram from  score_programas where Program='"+m02+"'", engine.connect())
        CitizenScore3yearsProgram=scrores_3years.values.tolist()[0][0]
        EnglishScore3yearsProgram=scrores_3years.values.tolist()[0][1]
        ReadingScore3yearsProgram=scrores_3years.values.tolist()[0][2]
        QuantitativeReasoningScore3yearsProgram=scrores_3years.values.tolist()[0][3]
        ComunicationScore3yearsProgram=scrores_3years.values.tolist()[0][4]
                                     
                                    
        #############################################################################################################################################
        
        dept1 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m06+"'", engine.connect())
        dept2 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m08+"'", engine.connect())
        lon1=dept1.values.tolist()[0][0]
        lat1=dept1.values.tolist()[0][1]
        lon2=dept2.values.tolist()[0][0]
        lat2=dept2.values.tolist()[0][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in kilometers is 6371
        km = 6371* c
        #############################################################################################################################################
        cluster_1=0
        cluster_2=0
        cluster_3=0
        cluster_4=0
        cluster = pd.read_sql("SELECT clusterdepartamentoescalado FROM departamento_detallado WHERE departamento='"+m08+"'", engine.connect())
        cluster_m = cluster.values.tolist()[0][0]
        if cluster_m == 1:
            cluster_1 = 1
        elif cluster_m == 2:
            cluster_2 = 1
        elif cluster_m == 3:
            cluster_3 = 1            
        elif cluster_m == 4:
            cluster_4 = 1           
   
        ###############################################################################################################################################
        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelQRPrueba = joblib.load('ModelQR.pkl')
        QR1 = np.round(ModelQRPrueba.predict([[hscore, hmvalue, QuantitativeReasoningScore3yearsProgram, agevalue, timesaber, mof, km, paydwayscholar, credito, paydwayparent, mama_1, mama_3, mama_4, mama_5, costo_1, costo_2, costo_3, costo_no]]),
                       0)
        X1 = int(QR1[0])
        
        
        return X1
        
  ##########################################################################################################
@app.callback(Output("mout_02", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m02", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value"),
                                               Input("m06", "value"),
                                               Input("m08", "value")])

                
                
def modelos2(n_clicks, m01,m02, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010,m06,m08):
    if n_clicks is None:
        return ""
    else:
        
        #############################################################################################################################################
        scrores_3years = pd.read_sql("select CitizenScore3yearsProgram, EnglishScore3yearsProgram,ReadingScore3yearsProgram,QuantitativeReasoningScore3yearsProgram,ComunicationScore3yearsProgram from  score_programas where Program='"+m02+"'", engine.connect())
        CitizenScore3yearsProgram=scrores_3years.values.tolist()[0][0]
        EnglishScore3yearsProgram=scrores_3years.values.tolist()[0][1]
        ReadingScore3yearsProgram=scrores_3years.values.tolist()[0][2]
        QuantitativeReasoningScore3yearsProgram=scrores_3years.values.tolist()[0][3]
        ComunicationScore3yearsProgram=scrores_3years.values.tolist()[0][4]
                                     
                                    
        #############################################################################################################################################
        
        dept1 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m06+"'", engine.connect())
        dept2 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m08+"'", engine.connect())
        lon1=dept1.values.tolist()[0][0]
        lat1=dept1.values.tolist()[0][1]
        lon2=dept2.values.tolist()[0][0]
        lat2=dept2.values.tolist()[0][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in kilometers is 6371
        km = 6371* c
        #############################################################################################################################################
        cluster_1=0
        cluster_2=0
        cluster_3=0
        cluster_4=0
        cluster = pd.read_sql("SELECT clusterdepartamentoescalado FROM departamento_detallado WHERE departamento='"+m08+"'", engine.connect())
        cluster_m = cluster.values.tolist()[0][0]
        if cluster_m == 1:
            cluster_1 = 1
        elif cluster_m == 2:
            cluster_2 = 1
        elif cluster_m == 3:
            cluster_3 = 1            
        elif cluster_m == 4:
            cluster_4 = 1           

        ###############################################################################################################################################
        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelRE = joblib.load('ModelRE.pkl')
        RE=np.round(ModelRE.predict([[
                                        hscore,
                                        hmvalue,
                                        ReadingScore3yearsProgram,
                                        agevalue,
                                        timesaber,
                                        mof,
                                        km,
                                        paydwayscholar,
                                        credito,
                                        paydwayparent,
                                        mama_1,
                                        mama_3,
                                        mama_4,
                                        mama_5,
                                        costo_1,
                                        costo_2,
                                        costo_3,
                                        costo_no
                                        ]]),0)
        READING=int(RE[0])
        X2 = READING

        
        return X2

 ##########################################################################################################
@app.callback(Output("mout_03", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m02", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value"),
                                               Input("m06", "value"),
                                               Input("m08", "value")])

                
                
def modelos3(n_clicks, m01,m02, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010,m06,m08):
    if n_clicks is None:
        return ""
    else:

        #############################################################################################################################################
        scrores_3years = pd.read_sql("select CitizenScore3yearsProgram, EnglishScore3yearsProgram,ReadingScore3yearsProgram,QuantitativeReasoningScore3yearsProgram,ComunicationScore3yearsProgram from  score_programas where Program='"+m02+"'", engine.connect())
        CitizenScore3yearsProgram=scrores_3years.values.tolist()[0][0]
        EnglishScore3yearsProgram=scrores_3years.values.tolist()[0][1]
        ReadingScore3yearsProgram=scrores_3years.values.tolist()[0][2]
        QuantitativeReasoningScore3yearsProgram=scrores_3years.values.tolist()[0][3]
        ComunicationScore3yearsProgram=scrores_3years.values.tolist()[0][4]
                                     
                                    
        #############################################################################################################################################
        
        dept1 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m06+"'", engine.connect())
        dept2 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m08+"'", engine.connect())
        lon1=dept1.values.tolist()[0][0]
        lat1=dept1.values.tolist()[0][1]
        lon2=dept2.values.tolist()[0][0]
        lat2=dept2.values.tolist()[0][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in kilometers is 6371
        km = 6371* c
        #############################################################################################################################################
        cluster_1=0
        cluster_2=0
        cluster_3=0
        cluster_4=0
        cluster = pd.read_sql("SELECT clusterdepartamentoescalado FROM departamento_detallado WHERE departamento='"+m08+"'", engine.connect())
        cluster_m = cluster.values.tolist()[0][0]
        if cluster_m == 1:
            cluster_1 = 1
        elif cluster_m == 2:
            cluster_2 = 1
        elif cluster_m == 3:
            cluster_3 = 1            
        elif cluster_m == 4:
            cluster_4 = 1           

        ###############################################################################################################################################
        hscore = 100
        hmvalue = 100
        hinglesvalue = 100
        hinglesvalue = m05
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelEN = joblib.load('ModelEN.pkl')
        EN=np.round(ModelEN.predict([[  hscore,
                                        hinglesvalue,
                                        EnglishScore3yearsProgram,
                                        agevalue,
                                        timesaber,
                                        mof,
                                        km,
                                        paydwayscholar,
                                        credito,
                                        paydwayparent,
                                        mama_1,
                                        mama_3,
                                        mama_4,
                                        mama_5,
                                        cluster_1,
                                        cluster_2,
                                        cluster_3,
                                        cluster_4
                                     ]]),0)
        ENGLISH=int(EN[0])
        X3 = ENGLISH
        return X3

     ##########################################################################################################
@app.callback(Output("mout_04", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m02", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value"),
                                               Input("m06", "value"),
                                               Input("m08", "value")])

                
                
def modelos4(n_clicks, m01,m02, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010,m06,m08):
    if n_clicks is None:
        return ""
    else:

        #############################################################################################################################################
        scrores_3years = pd.read_sql("select CitizenScore3yearsProgram, EnglishScore3yearsProgram,ReadingScore3yearsProgram,QuantitativeReasoningScore3yearsProgram,ComunicationScore3yearsProgram from  score_programas where Program='"+m02+"'", engine.connect())
        CitizenScore3yearsProgram=scrores_3years.values.tolist()[0][0]
        EnglishScore3yearsProgram=scrores_3years.values.tolist()[0][1]
        ReadingScore3yearsProgram=scrores_3years.values.tolist()[0][2]
        QuantitativeReasoningScore3yearsProgram=scrores_3years.values.tolist()[0][3]
        ComunicationScore3yearsProgram=scrores_3years.values.tolist()[0][4]
                                     
                                    
        #############################################################################################################################################
        
        dept1 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m06+"'", engine.connect())
        dept2 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m08+"'", engine.connect())
        lon1=dept1.values.tolist()[0][0]
        lat1=dept1.values.tolist()[0][1]
        lon2=dept2.values.tolist()[0][0]
        lat2=dept2.values.tolist()[0][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in kilometers is 6371
        km = 6371* c
        #############################################################################################################################################
        cluster_1=0
        cluster_2=0
        cluster_3=0
        cluster_4=0
        cluster = pd.read_sql("SELECT clusterdepartamentoescalado FROM departamento_detallado WHERE departamento='"+m08+"'", engine.connect())
        cluster_m = cluster.values.tolist()[0][0]
        if cluster_m == 1:
            cluster_1 = 1
        elif cluster_m == 2:
            cluster_2 = 1
        elif cluster_m == 3:
            cluster_3 = 1            
        elif cluster_m == 4:
            cluster_4 = 1           
    
            
        ###############################################################################################################################################
        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelCOMMUNICATION = joblib.load('ModelCOMMUNICATION.pkl')
        COMM=np.round(ModelCOMMUNICATION.predict([[hscore,
                                                    hmvalue,
                                                    ComunicationScore3yearsProgram,
                                                    agevalue,
                                                    timesaber,
                                                    mof,
                                                    km,
                                                    paydwayscholar,
                                                    credito,
                                                    paydwayparent,
                                                    mama_1,
                                                    mama_3,
                                                    mama_4,
                                                    mama_5,
                                                    cluster_1,
                                                    cluster_2,
                                                    cluster_3,
                                                    cluster_4
                                                  ]]),0)
        COMMUNICATION=int(COMM[0])

        X4 = COMMUNICATION

        return X4

     ##########################################################################################################
@app.callback(Output("mout_05", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m02", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value"),
                                               Input("m06", "value"),
                                               Input("m08", "value")])

                
                
def modelos5(n_clicks, m01,m02, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010,m06,m08):
    if n_clicks is None:
        return ""
    else:

         #############################################################################################################################################
        scrores_3years = pd.read_sql("select CitizenScore3yearsProgram, EnglishScore3yearsProgram,ReadingScore3yearsProgram,QuantitativeReasoningScore3yearsProgram,ComunicationScore3yearsProgram from  score_programas where Program='"+m02+"'", engine.connect())
        CitizenScore3yearsProgram=scrores_3years.values.tolist()[0][0]
        EnglishScore3yearsProgram=scrores_3years.values.tolist()[0][1]
        ReadingScore3yearsProgram=scrores_3years.values.tolist()[0][2]
        QuantitativeReasoningScore3yearsProgram=scrores_3years.values.tolist()[0][3]
        ComunicationScore3yearsProgram=scrores_3years.values.tolist()[0][4]
                                     
                                    
        #############################################################################################################################################
        
        dept1 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m06+"'", engine.connect())
        dept2 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m08+"'", engine.connect())
        lon1=dept1.values.tolist()[0][0]
        lat1=dept1.values.tolist()[0][1]
        lon2=dept2.values.tolist()[0][0]
        lat2=dept2.values.tolist()[0][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in kilometers is 6371
        km = 6371* c
        #############################################################################################################################################
        cluster_1=0
        cluster_2=0
        cluster_3=0
        cluster_4=0
        cluster = pd.read_sql("SELECT clusterdepartamentoescalado FROM departamento_detallado WHERE departamento='"+m08+"'", engine.connect())
        cluster_m = cluster.values.tolist()[0][0]
        if cluster_m == 1:
            cluster_1 = 1
        elif cluster_m == 2:
            cluster_2 = 1
        elif cluster_m == 3:
            cluster_3 = 1            
        elif cluster_m == 4:
            cluster_4 = 1           
      
            
        ###############################################################################################################################################
        hscore = 100
        hmvalue = 100
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0


        ModelGLOBAL = joblib.load('ModelGLOBAL.pkl')
        GLOBALSCORE=np.round(ModelGLOBAL.predict([[
                                                        hscore,
                                                        hmvalue,
                                                        CitizenScore3yearsProgram,
                                                        agevalue,
                                                        timesaber,
                                                        mof,
                                                        km,
                                                        paydwayscholar,
                                                        credito,
                                                        paydwayparent,
                                                        mama_1,
                                                        mama_3,
                                                        mama_4,
                                                        mama_5,
                                                        cluster_1,
                                                        cluster_2,
                                                        cluster_3,
                                                        cluster_4,
                                                        costo_1,
                                                        costo_2,
                                                        costo_3,
                                                        costo_no
                                                  ]]),0)
        GLOBAL=int(GLOBALSCORE[0])
        X5 = GLOBAL
        return X5

     ##########################################################################################################
@app.callback(Output("mout_06", "children"), [Input("m016", "n_clicks"),
                                               Input("m01", "value"),
                                               Input("m02", "value"),
                                               Input("m03", "value"),
                                               Input("m05", "value"),
                                               Input("m07", "value"),
                                               Input("m014", "value"),
                                               Input("m015", "value"),
                                               Input("m012", "value"),
                                               Input("m013", "value"),
                                               Input("m09", "value"),
                                               Input("m011", "value"),
                                               Input("m010", "value"),
                                               Input("m06", "value"),
                                               Input("m08", "value")])

                
                
def modelos6(n_clicks, m01,m02, m03, m05, m07,m014, m015,m012,m013,m09,m011, m010,m06,m08):
    if n_clicks is None:
        return ""
    else:

        #############################################################################################################################################
        scrores_3years = pd.read_sql("select CitizenScore3yearsProgram, EnglishScore3yearsProgram,ReadingScore3yearsProgram,QuantitativeReasoningScore3yearsProgram,ComunicationScore3yearsProgram from  score_programas where Program='"+m02+"'", engine.connect())
        CitizenScore3yearsProgram=scrores_3years.values.tolist()[0][0]
        EnglishScore3yearsProgram=scrores_3years.values.tolist()[0][1]
        ReadingScore3yearsProgram=scrores_3years.values.tolist()[0][2]
        QuantitativeReasoningScore3yearsProgram=scrores_3years.values.tolist()[0][3]
        ComunicationScore3yearsProgram=scrores_3years.values.tolist()[0][4]
                                     
                                    
        #############################################################################################################################################
        
        dept1 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m06+"'", engine.connect())
        dept2 = pd.read_sql("SELECT Lat,Lon FROM departamento_detallado where Departamento='"+m08+"'", engine.connect())
        lon1=dept1.values.tolist()[0][0]
        lat1=dept1.values.tolist()[0][1]
        lon2=dept2.values.tolist()[0][0]
        lat2=dept2.values.tolist()[0][1]
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        # Radius of earth in kilometers is 6371
        km = 6371* c
        #############################################################################################################################################
        cluster_1=0
        cluster_2=0
        cluster_3=0
        cluster_4=0
        cluster = pd.read_sql("SELECT clusterdepartamentoescalado FROM departamento_detallado WHERE departamento='"+m08+"'", engine.connect())
        cluster_m = cluster.values.tolist()[0][0]
        if cluster_m == 1:
            cluster_1 = 1
        elif cluster_m == 2:
            cluster_2 = 1
        elif cluster_m == 3:
            cluster_3 = 1            
        elif cluster_m == 4:
            cluster_4 = 1           
        elif cluster_m == 4:
            cluster_4 = 1        
            
        ###############################################################################################################################################
        hscore = 100
        hmvalue = 100
        hinglesvalue = 100
        hinglesvalue = m05
        agevalue = 30
        saber11 = 2014
        saberpro = 2019
        paydwayscholar = 0
        paydwayparent = 0
        mof = 0
        credito=0
        mama_1 = 0
        mama_3 = 0
        mama_4 = 0
        mama_5 = 0
        mama_m = m012
        credito_m= m014
        costo = m013
        costo_1 = 0
        costo_2 = 0
        costo_3 = 0
        costo_no = 0
        genero = m010
        if genero == 'M':
            mof = 1
        else:
            mof = 0
        hmvalue = float(m03)
        hscore = float(m01)
        agevalue = float(m07)
        saber11 = float(m09)
        saberpro = float(m011)
        timesaber = saberpro -saber11
        
        paydway = m015
###################################
        if paydway == 'Parents':
            paydwayparent = 1
        else:
            if paydway == 'Scholarship':
                paydwayscholar = 1
            else:
                paydwayparent = 0
                paydwayscholar = 0
 ####################################
        if credito_m == 'YES':
            credito = 1
        else:
            credito = 0
#########################################
        if mama_m == '1':
            mama_1 = 1
        else:
            if mama_m == '3':
                mama_3 = 1
            else:
                if mama_m == '4':
                    mama_4 = 1
                else:
                    if mama_m == '5':
                        mama_5 = 1
                    else:
                        mama_1 = 0
                        mama_3 = 0
                        mama_4 = 0
                        mama_5 = 0
#########################################
        if costo == '1':
            costo_1 = 1
        else:
            if costo == '2':
                costo_2 = 1
            else:
                if costo == '3':
                    costo_3 = 1
                else:
                    if costo == '5':
                        costo_no = 1
                    else:
                        costo_1 = 0
                        costo_2 = 0
                        costo_3 = 0
                        costo_no = 0
 

        ModelCI = joblib.load('ModelCI.pkl')
        CI=np.round(ModelCI.predict([[
                                    hscore,
                                    hmvalue,
                                    CitizenScore3yearsProgram,
                                    agevalue,
                                    timesaber,
                                    mof,
                                    km,
                                    paydwayscholar,
                                    credito,
                                    paydwayparent,
                                    mama_1,
                                    mama_3,
                                    mama_4,
                                    mama_5,
                                    cluster_1,
                                    cluster_2,
                                    cluster_3,
                                    cluster_4,
                                    costo_1,
                                    costo_2,
                                    costo_3,
                                    costo_no
                                    ]]),0)
        CITIZEN=int(CI[0])
        X6 = CITIZEN
        
        return X6
