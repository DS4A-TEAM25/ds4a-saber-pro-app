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


####################################################################
posenglish_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("posenglish", className="mr-2"),
                dbc.Input(type="text", placeholder="posenglish"),
            ],
            className="mr-3",
        )

    ],
    inline=True,
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
inline = True,
)

###########################################################################
scoreMathHighSchool_form = dbc.Form(
    [
dbc.FormGroup(
    [
        dbc.Label("ScoreMathHighSchool", className="mr-2"),
        dbc.Input(type="text", placeholder="ScoreMathHighSchool"),
    ],
    className="mr-3",
)
    ],
    inline=True,
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
    inline=True,
)

############################################################################
ScoreEnglishHighSchool_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("ScoreEnglishHighSchool", className="mr-2"),
                dbc.Input(type="text", placeholder="ScoreEnglishHighSchool"),
            ],
            className="mr-3",
        )

    ],
    inline=True,
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
    inline=True,
)


#################################################################################

age_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("age", className="mr-2"),
                dbc.Input(type="text", placeholder="age"),
            ],
            className="mr-3",
        )

    ],
    inline=True,
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
    inline=True,
)


#####################################################################################

years11_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber11 was presented", className="mr-2"),
                dbc.Input(type="text", placeholder="Year when Saber11 was presented"),
            ],
            className="mr-3",
        )

    ],
    inline=True,
)


##########################################################################################

gender_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Gender", className="mr-2"),
                dbc.Input(type="text", placeholder="Gender"),
            ],
            className="mr-3",
        )

    ],
    inline=True,
)


##########################################################################################

year_pro_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber Pro was presented", className="mr-2"),
                dbc.Input(type="text", placeholder="Year when Saber pro was presented"),
            ],
            className="mr-3",
        )

    ],
    inline=True,
)


#############################################################################################
mother_level_form = dbc.Form(
    [
        dbc.FormGroup(
            [
                dbc.Label("Year when Saber11 was presented", className="mr-2"),
                dbc.Input(type="text", placeholder="Year when Saber11 was presented"),
            ],
            className="mr-3",
        )

    ],
    inline=True,
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
    inline=True,
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
    inline=True,
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
    inline=True,
)

##################################################################

suerte_botton = dbc.Button("Wish me luck!", color="primary")

##################################################################################################################

row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(posenglish_form),
                dbc.Col(program_form),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(scoreMathHighSchool_form),
                dbc.Col(university_form),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(ScoreEnglishHighSchool_form),
                dbc.Col(state_form),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(age_form),
                dbc.Col(state_uni_form),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(years11_form),
                dbc.Col(gender_form),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(year_pro_form),
                dbc.Col(mother_level_form),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(value_form),
                dbc.Col(credit_form),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(help_form),
                
            ]
        ),        
    ]
)



layout = html.Div([
    html.H1(X1),
    row,
    suerte_botton
])

