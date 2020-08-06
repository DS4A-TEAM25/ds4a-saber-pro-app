import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app


layout =  html.Div(
        [
            
            #TITLE AND EXPLANATION OF THIS PAGE
            html.Div(
                [ html.H1(" Which Factors Matter to Saber PRO Scores?", className="ml-3", 
                         style = {'font-size': '42px' ,'color': '4d4d4d', 
                                    'text-shadow': '2px 8px 6px rgba(0,0,0,0.2), 0px -5px 35px rgba(255,255,255,0.3)'}),
                 html.Hr(className="my-2"),
                 html.H5(" In order to assess the main factors that explain undergrad"
                        " performance on the Saber-Pro tests, we explored different models"
                        " such as  Random Forest and Spatial models"  , className="mb-3 mt-3 ml-3"),
                 
                  html.H5(" Below we present some of the key results:"  , className="mb-4 mt-3 ml-3"),
                 
                 
                 
                 
                     #SPATIAL MODEL JUMOTRON
                     html.Div([ dbc.Jumbotron(
                         [
                             dbc.Container(
                                            [
                                                html.H1("Student-Level Factors"),
                                                html.P(
                                                    "To explore which factors affect student performance on the SABER PRO we explored several models. One of these were a series of Random Forest models to predict each of the SABER PRO scores. All of the models suggested that student characterstics are the most important variables when it comes to predicting results on the test.",
                                                    className="lead",
                                                ),
                                                dbc.Button("Learn More about the Model", id="open-body-scroll2", color="primary"),
                                                dbc.Modal(
                                                    [
                                                        dbc.ModalHeader("What is a Random Forest Model?"),
                                                        dbc.ModalBody("We can understand the Random Forest algorithm as an ensemble of other algorithms known as trees, where these trees are all slightly different from one another. The fundamental idea behind a random forest is to combine many decision trees into a single model. Decision trees are an extremely intuitive ways to classify or label objects: you simply ask a series of questions designed to zero-in on the classification. The binary splitting makes this process of classification extremely efficient: in a well-constructed tree, each question will cut the number of options by approximately half, very quickly narrowing the options even among a large number of classes. The trick, of course, comes in deciding which questions to ask at each step. Our Random Forest models, one for each score, had accuracies between 85 and 93% and 14 input variables were used."),
                                                        dbc.ModalFooter(
                                                            dbc.Button(
                                                                "Close", id="close-body-scroll2", className="ml-auto"
                                                            )
                                                        ),
                                                    ], id="modal-body-scroll2",
                                                    scrollable=True,
                                                ),
                                                html.Hr(className="my-2"),
                                                
                                                dbc.Row([
                                                
                                                dbc.Col([
                                                        
                                                        dbc.Row(
                                                        html.Img(src='/assets/saber11.png', style={'height':'auto', 'width':'80%'}, className="ml-3"), ), 
                                                        
                                                        
                                                        dbc.Row(
                                                        html.H5(children='Good global, Math and English results  on  the Saber 11 test , have a positive impact on Saber Pro scores.This suggests that early intervention before students start college is key to helping students take the most advantage out of higher education and perform better on the SABER PRO. Student that had weaker scores should be given additional support before taking this exam.' 
                                     ) 
                                                    
                    , className="mb-4 mt-5")]
                                                    
                                                    ),
                                                    
                                                    dbc.Col([
                                                        
                                                        dbc.Row(
                                                        html.Img(src='/assets/mother_education.png', style={'height':'auto', 'width':'80%'}, className="mr-3"), ), 
                                                        
                                                        
                                                        dbc.Row(
                                                        html.H5(children='Student family background is key! For example, the students mother’s education has an impact on the score. The better educated the mother, the better the scores. We should understand and survey student backgrounds to increase support for first-generation college students.' 
                                     ) 
                                                    
                    , className="mb-4 mt-5")]
                                                    
                                                    ),
                                                            
                                                    ]),
                                                
                                                dbc.Row([
                                                
                                                        
                                                        dbc.Row(
                                                        html.Img(src='/assets/programas.png', style={'height':'600', 'width':'400', 'display': 'block', 'margin-left': '5', 'padding-left': '200px'}, className="ml-3"), ), 
                                                        
                                                        
                                                        dbc.Row(
                                                        html.H5(children='The average score obtained by the student’s academic program in the last 3 years was important. Academic Programs with historically low results should be identified and programs should be implemented to assess and improve their quality.' 
                                    ,style={'padding-left': '200px', 'padding-right': '300px'} ) 
                                                    
                    , className="mb-4 mt-5 ml-6")

                                                            
                                                    ]), 
                                            ],
                                            fluid=True,
                                        )
                                    ],
                                    fluid=True,
                                )

                     ]),
  
                     #SPATIAL MODEL JUMOTRON
                     html.Div([ dbc.Jumbotron(
                         [
                             dbc.Container(
                                            [
                                                html.H1("Spatial Model"),
                                                html.P(
                                                    "Spatial effects might be one important factor that could also influence these results. We ran spatial autocorrelation models and found that the spatial distribution of the performance on the tests was not random, meaning that groups of departments with similar SABER PRO performance were closer together geographically. We found a high degree of spatial autocorrelation in our data, which suggests that the Government should identify which department represents a neighbor or peer in terms of its similarity in the quality of education, measured by the results of the Saber tests. This allows for government entities to generate more impactful policies in terms of possible externalities which could have a positive influence on the different clusters, and in this manner contribute to improving the quality of education throughout the country in general.",
                                                    className="lead",
                                                ),
                                                dbc.Button("Learn More about the Model", id="open-body-scroll", color="primary"),
                                                dbc.Modal(
                                                    [
                                                        dbc.ModalHeader("What are Spatial Autocorrelation models?"),
                                                        dbc.ModalBody("Spatial models allows us to explore and to test spatial autocorrelation in the data. The concept of spatial autocorrelation relates to the combination of two types of similarity: spatial similarity and attribute similarity. Although there are many different measures of spatial autocorrelation, they all combine these two types of simmilarity into a summary measure.In spatial autocorrelation analysis, the spatial weights are used to formalize the notion of spatial similarity. Spatial weights are mathematical structures used to represent spatial relationships. Many spatial analytics, such as spatial autocorrelation statistics and regionalization algorithms rely on spatial weights. Generally speaking, a spatial weight wij expresses the notion of a geographical relationship between locations i and j. These relationships can be based on a number of criteria including contiguity, geospatial distance and general distances. The Spatial Autocorrelation (Global Moran's I) tool measures spatial autocorrelation based on both feature locations and feature values simultaneously. Given a set of features and an associated attribute, it evaluates whether the pattern expressed is clustered, dispersed, or random. We obtained a Moran's I of, which suggest a degree of spatial autocorrelation. The following are the goodness of fit measures of our model: R-squared=0.9066, Rbar-squared=0.8886, sigma^2 = 6.7193, Nobs, Nvars= 32, 6, log-likelihood =-64.844943, of iterations= 13"),
                                                        dbc.ModalFooter(
                                                            dbc.Button(
                                                                "Close", id="close-body-scroll", className="ml-auto"
                                                            )
                                                        ),
                                                    ], id="modal-body-scroll",
                                                    scrollable=True,
                                                ),
                                                html.Hr(className="my-2"),
                                                
                                                dbc.Row([
                                                
                                                dbc.Col([
                                                        
                                                        dbc.Row(
                                                        html.Img(src='/assets/EnglScores.png', style={'height':'auto', 'width':'70%'}, className="ml-3"), ), 
                                                        
                                                        
                                                        dbc.Row(
                                                        html.H5(children='English results of Saber-Pro test by departments. Similar colors represent the clusters of the departments.Lighter colored clusters represent better scores in the overall results of Saber Pro tests.'
                                     ) 
                                                    
                    , className="mb-4 mt-5")]
                                                    
                                                    ),
                                                    
                                                    dbc.Col([
                                                        
                                                        dbc.Row(
                                                        html.Img(src='/assets/globalSc.png', style={'height':'auto', 'width':'70%'}, className="ml-3"), ), 
                                                        
                                                        
                                                        dbc.Row(
                                                        html.H5(children='Global score results of Saber-Pro test by departments. Similar colors represent the clusters of the departments.Lighter colored clusters represent better scores in the overall results of Saber Pro tests.'
                                     ) 
                                                    
                    , className="mb-4 mt-5")]
                                                    
                                                    ),
                                                            
                                                    ]),   
                                            ],
                                            fluid=True,
                                        )
                                    ],
                                    fluid=True,
                                )

                     ]),

        ]
    )
        ]
)
            

##################### Callbacks ######################################
#MODAL CALLBACKS THAT APPEAR WHEN YOU CLICK ON THE HELP BUTTON ON EACH GRAPH


@app.callback(Output("modal-body-scroll", "is_open"),
              [
                  Input("open-body-scroll", "n_clicks"),
                  Input("close-body-scroll", "n_clicks"),
              ],
              [State("modal-body-scroll", "is_open")],
             )

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(Output("modal-body-scroll2", "is_open"),
              [
                  Input("open-body-scroll2", "n_clicks"),
                  Input("close-body-scroll2", "n_clicks"),
              ],
              [State("modal-body-scroll2", "is_open")],
             )

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open
