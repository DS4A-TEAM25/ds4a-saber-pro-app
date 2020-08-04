import dash
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

#Use if you want to change the style later or if you wanna make your own css
BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/simplex/bootstrap.min.css"
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
CUSTOM_STYLE = "/assets/style.css"
external_stylesheets=[BS, FONT_AWESOME, CUSTOM_STYLE]



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True
