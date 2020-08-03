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


# Create Engine and connect to DB
engine = create_engine('postgresql://admin:ds4a@data-team25.c6tqz0tiazsw.us-east-2.rds.amazonaws.com/project_ds4a')

#Define variables for reactive components
#Departamento options
departamento_options_1 = get_unique(engine, 'pro_data', "estu_inst_departamento")


ModelQRPrueba = joblib.load('ModelQR.pkl')
QR1=np.round(ModelQRPrueba.predict([[59, 59, 59, 22, 6, 0,1,1,1,1,0,1,0,0,0,0,0,0]]),0)
QR1
X1=int(QR1[0])
X1


#######****Corregir_nombre#############################################################
posenglish_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("posenglish", className="mr-2"),
                dbc.Input(id="m01", type="number", placeholder="posenglish", min=0, max=1000, step=0.01),
            ],
            className="mr-3",
        )

    ],
)

###################################################################
program_form = dbc.Form(
    [

    dbc.FormGroup(
        [
            dbc.Label("Program", className="mr-2"),
            dbc.Input(id="m02", type="text", placeholder="Program"),
        ],
        className="mr-3",
    )
    ],
)

#####****######################################################################
scoreMathHighSchool_form = dbc.Form(
    [
dbc.FormGroup(
    [
        dbc.Label("ScoreMathHighSchool", className="mr-2"),
        dbc.Input(id="m03", type="number", placeholder="ScoreMathHighSchool", min=0, max=150, step=0.01),
    ],
    className="mr-3",
)
    ],
)

##############################################################################
university_form = dbc.Form(
    [
        dbc.FormGroup(
            [
    dbc.Label("University", className="mr-2"),
    dbc.Input(id="m04", type="text", placeholder="University"),
            ],
            className="mr-3",
        )
    ],
)

############################################################################
ScoreEnglishHighSchool_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("ScoreEnglishHighSchool", className="mr-2"),
                dbc.Input(id="m05", type="number", placeholder="ScoreEnglishHighSchool", min=0, max=150, step=0.01),
            ],
            className="mr-3",
        )

    ],
)


##############################################################################

state_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("State Where you Live", className="mr-2"),
                dbc.Input(id="m06", type="text", placeholder="State Where you Live"),
            ],
            className="mr-3",
        )

    ],
)


###########****######################################################################

age_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("age", className="mr-2"),
                dbc.Input(id="m07", type="number", placeholder="age", min=0, max=60, step=1),
            ],
            className="mr-3",
        )

    ],
)


##################################################################################

state_uni_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("State Where you Study", className="mr-2"),
                dbc.Input(id="m08", type="text", placeholder="State Where you Study"),
            ],
            className="mr-3",
        )

    ],
)


#####################################################################################

years11_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber11 was presented", className="mr-2"),
                dbc.Input(id="m09", type="number", placeholder="Year when Saber11 was presented", min=1990, max=2019, step=1),
            ],
            className="mr-3",
        )

    ],
)


##########################################################################################

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



##########################################################################################

year_pro_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber Pro was presented", className="mr-2"),
                dbc.Input(id="m011", type="number", placeholder="Year when Saber pro was presented", min=2016, max=2025, step=1),
            ],
            className="mr-3",
        )

    ],
)


#############################################################################################
mother_level_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("MotherEducation", className="mr-2"),
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


##########################################################################################################

value_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Value payd in the university per semester", className="mr-2"),
                dbc.Select(
                    id="m013", 
                    options=[
                                {"label": "Menos de 500 mil'", "value": "1"},
                                {"label": "0.5M-4M", "value": "2"},
                                {"label": "4M-7M", "value": "3"},
                                {"label": "7+", "value": "4"},
                                {"label": "No pago matricula", "value": "5"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)

#############################################################################################################

credit_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("VDid you use a credit to pay university?", className="mr-2"),
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



##################################################################################################################
help_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Did your parents help you to pay the university?", className="mr-2"),
                dbc.Select(
                    id="m015", 
                    options=[
                                {"label": "Parents", "value": "Parents"},
                                {"label": "Scholarship", "value": "Scholarship"},
                                {"label": "Myself", "value": "Myself"},
                    ],
                )



            ],
            className="mr-3",
        )

    ],
)
##################################################################

suerte_botton = dbc.Button("Wish me luck!", color="primary", id="m016",)

##################################################################################################################
##################################################################################################################
tarjeta1 = dbc.Card(
    dbc.CardBody(
        [
            posenglish_form,
            scoreMathHighSchool_form,
            ScoreEnglishHighSchool_form,
            age_form,
            years11_form,
            year_pro_form,
            value_form,
            help_form,
        ]
    )
)

tarjeta2 = dbc.Card(
    dbc.CardBody(
        [
            program_form,
            university_form,
            state_form,
            state_uni_form,
            gender_form,
            mother_level_form,
            credit_form,
            suerte_botton,
        ]
    )
)



row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(tarjeta1, color="secondary", outline=True)),
        dbc.Col(dbc.Card(tarjeta2, color="secondary", outline=True)),
    ],
    className="mb-4",
)


forumulario = html.Div([row_1])



#######################################################################################
#######################################################################################



card_content_1 = [
    dbc.CardHeader("Quantitative Reasoning"),
    dbc.CardBody(
        [
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your program",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your University",
                className="card-text",
            ),
            html.P(
                "Average Score Expected for your State",
                className="card-text",
            ),

        ]
    ),
]

card_content_2 = [
    dbc.CardHeader("Citizen competence"),
    dbc.CardBody(
        [
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your program",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your University",
                className="card-text",
            ),
            html.P(
                "Average Score Expected for your State",
                className="card-text",
            ),

        ]
    ),
]

card_content_3 = [
    dbc.CardHeader("Critical Lecture"),
    dbc.CardBody(
        [
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your program",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your University",
                className="card-text",
            ),
            html.P(
                "Average Score Expected for your State",
                className="card-text",
            ),

        ]
    ),
]

card_content_4 = [
    dbc.CardHeader("English"),
    dbc.CardBody(
        [
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your program",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your University",
                className="card-text",
            ),
            html.P(
                "Average Score Expected for your State",
                className="card-text",
            ),

        ]
    ),
]


card_content_5 = [
    dbc.CardHeader("model 5"),
    dbc.CardBody(
        [
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your program",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your University",
                className="card-text",
            ),
            html.P(
                "Average Score Expected for your State",
                className="card-text",
            ),

        ]
    ),
]

card_content_6 = [
    dbc.CardHeader("model 6"),
    dbc.CardBody(
        [
            html.P(
                "Score expected for you:",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your program",
                className="card-text",
            ),
            html.P(
                "Average Score expected for your University",
                className="card-text",
            ),
            html.P(
                "Average Score Expected for your State",
                className="card-text",
            ),

        ]
    ),
]


row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_1, color="secondary", outline=True)),
        dbc.Col(dbc.Card(card_content_2, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_3, color="secondary", outline=True)),
        dbc.Col(dbc.Card(card_content_4, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content_5, color="secondary", outline=True)),
        dbc.Col(dbc.Card(card_content_6, color="secondary", outline=True)),
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

layout = html.Div([
    html.H1("I will present my exam soon and i want to check how is going to be my result"),
    html.H3("resultado del modelo", id="mout_01"),
    esquema,   
])
   
                                    
@app.callback(
    Output("mout_01", "children"), [Input("m016", "n_clicks")]
)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        return f"Clicked {n} times."
