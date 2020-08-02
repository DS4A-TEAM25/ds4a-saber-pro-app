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
                dbc.Input(type="number", placeholder="posenglish", min=0, max=1000, step=0.01),
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
            dbc.Input(type="text", placeholder="Program"),
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
        dbc.Input(type="number", placeholder="ScoreMathHighSchool", min=0, max=150, step=0.01),
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
    dbc.Input(type="text", placeholder="University"),
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
                dbc.Input(type="number", placeholder="ScoreEnglishHighSchool", min=0, max=150, step=0.01),
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
                dbc.Input(type="text", placeholder="State Where you Live"),
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
                dbc.Input(type="number", placeholder="age", min=0, max=60, step=1),
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
                dbc.Input(type="text", placeholder="State Where you Study"),
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
                dbc.Input(type="number", placeholder="Year when Saber11 was presented", min=1990, max=2019, step=1),
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
                    id="gender",
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
                dbc.Input(type="number", placeholder="Year when Saber pro was presented", min=2016, max=2025, step=1),
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
                    id="nother_lev",
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
                dbc.Input(type="text", placeholder="Value payd in the university per semester"),
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
                dbc.Label("Did you use a credit to pay university?", className="mr-2"),
                dbc.Input(type="text", placeholder="Did you use a credit to pay university?"),
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
                dbc.Label("Did your parents help you to pay the university", className="mr-2"),
                dbc.Input(type="text", placeholder="Did your parents help you to pau the university"),
            ],
            className="mr-3",
        )

    ],
)

##################################################################

suerte_botton = dbc.Button("Wish me luck!", color="primary")

##################################################################################################################
##################################################################################################################
posenglish_form_card = dbc.Card(
    dbc.CardBody(
        [
            posenglish_form            
        ]
    )
)

program_form_card = dbc.Card(
    dbc.CardBody(
        [
            program_form            
        ]
    )
)

scoreMathHighSchool_form_card = dbc.Card(
    dbc.CardBody(
        [
            scoreMathHighSchool_form            
        ]
    )
)

university_form_card = dbc.Card(
    dbc.CardBody(
        [
            university_form            
        ]
    )
)

ScoreEnglishHighSchool_form_card = dbc.Card(
    dbc.CardBody(
        [
            ScoreEnglishHighSchool_form            
        ]
    )
)

pstate_form_card = dbc.Card(
    dbc.CardBody(
        [
            state_form            
        ]
    )
)

age_form_card = dbc.Card(
    dbc.CardBody(
        [
            age_form            
        ]
    )
)

state_uni_form_card = dbc.Card(
    dbc.CardBody(
        [
            state_uni_form            
        ]
    )
)

years11_form_card = dbc.Card(
    dbc.CardBody(
        [
            years11_form            
        ]
    )
)

gender_form_card = dbc.Card(
    dbc.CardBody(
        [
            gender_form            
        ]
    )
)

year_pro_form_card = dbc.Card(
    dbc.CardBody(
        [
            year_pro_form            
        ]
    )
)

mother_level_form_card = dbc.Card(
    dbc.CardBody(
        [
            mother_level_form            
        ]
    )
)

value_form_card = dbc.Card(
    dbc.CardBody(
        [
            value_form            
        ]
    )
)

credit_form_card = dbc.Card(
    dbc.CardBody(
        [
            credit_form            
        ]
    )
)

help_form_card = dbc.Card(
    dbc.CardBody(
        [
            help_form            
        ]
    )
)

suerte_botton_card = dbc.Card(
    dbc.CardBody(
        [
            suerte_botton            
        ]
    )
)


row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(posenglish_form_card, color="secondary", outline=True)),
        dbc.Col(dbc.Card(program_form_card, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(scoreMathHighSchool_form_card, color="secondary", outline=True)),
        dbc.Col(dbc.Card(university_form_card, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(ScoreEnglishHighSchool_form_card, color="secondary", outline=True)),
        dbc.Col(dbc.Card(pstate_form_card, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_4 = dbc.Row(
    [
        dbc.Col(dbc.Card(age_form_card, color="secondary", outline=True)),
        dbc.Col(dbc.Card(state_uni_form_card, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_5 = dbc.Row(
    [
        dbc.Col(dbc.Card(years11_form_card, color="secondary", outline=True)),
        dbc.Col(dbc.Card(gender_form_card, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_6 = dbc.Row(
    [
        dbc.Col(dbc.Card(year_pro_form_card, color="secondary", outline=True)),
        dbc.Col(dbc.Card(mother_level_form_card, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_7 = dbc.Row(
    [
        dbc.Col(dbc.Card(value_form_card, color="secondary", outline=True)),
        dbc.Col(dbc.Card(credit_form_card, color="secondary", outline=True)),
    ],
    className="mb-4",
)

row_8 = dbc.Row(
    [
        dbc.Col(dbc.Card(help_form_card, color="secondary", outline=True)),
        dbc.Col(dbc.Card(suerte_botton_card, color="secondary", outline=True)),
    ],
    className="mb-4",
)

forumulario = html.Div([row_1, row_2, row_3,row_4, row_5, row_6,row_7, row_8])



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
    esquema,   
])

