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




layout = html.Div([
    html.H1(X1),    
])

