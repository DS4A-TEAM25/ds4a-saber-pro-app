import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    
    dbc.Container([
        
        dbc.Row([            
            dbc.Col(html.H1(children = ""
                            , style={'textAlign': 'center', 'background-image': 'url(/assets/banner.jpg)', #Banner
                                    'opacity': '0.2', '-ms-background-size': 'cover', 'padding':'75px', 
                                    'background-repeat': 'no-repeat', 
                                    'background-size': 'contain', 
                                     'background-position': 'center', 
                                    'position':'absolute', 
                                    'width':'100%', 
                                    'height':'50%', 
                                    'left':'0', 
                                    'top':'0', 
                                    'z-index':'-1', 
                                    }
                           ) 
                    , className="mb-5 mt-0")
        ]),
        
        dbc.Row([            
            dbc.Col(html.H1(children = "Welcome to the SABER PRO Exploratory dashboard", className="text-center", 
                           style = {'font-size': '36px' ,'color': '4d4d4d', 
                                    'text-shadow': '2px 8px 6px rgba(0,0,0,0.2), 0px -5px 35px rgba(255,255,255,0.3)'}) 
                    , className="mb-5 mt-0 p-0") #PAGE TITLE
        ]),

  
        dbc.Row([
            dbc.Col(html.H5(children='The \"Test on the Quality of Higher Education\" - SABER PRO – is a standarized test administered to students who are about to complete their undergraduate education in Colombia.'
                            ' Social, demographic, financial, and geographic factors can affect student scores on the SABER PRO'
                                     )
                    , className="mb-4 mt-5") #SABER PRO INFO
           
            ]),
        
        dbc.Row([
            dbc.Col(html.H5(children='This app allows you to explore the factors that drive SABER PRO scores and to compare how well different regions and higher education institutions perform.')
                    , className="mb-4") #APP OBJECTIVE
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='It consists of four main pages:'  
                           ' EXPLORE BY LOCATION allows you to compare SABER PRO scores across departments.'
                           ' EXPLORE BY UNIVERSITY allows you to see scores by higher education institution and compare them to other institutions.'
                           ' PREDICT SCORES allows you to input a set of student characeristics and predict how well a student will perform on the SABER PRO given these characteristics.'
                           ' WHICH FACTORS MATTER? summarizes the results of models we created to explain which factors drive SABER PRO scores.')
                    , className="mb-5") #CONTENT DESCRIPTION
        ]),

        

        dbc.Row([


            dbc.Col(dbc.Card(children=[html.H5(children='Access the code used to build this dashboard',
                                               className="text-center"),
                                       
                                       dbc.Button(
            html.Span([html.I(className="fab fa-github ml-0"), " GitHub"]), href="https://github.com/DS4A-TEAM25/ds4a-saber-pro-app", target="_blank",
                                                  color="primary",
                                                  className="mt-3"), #LINK TO OUR GITHUB REPO
 
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H5(children='Read about how we conducted our data analysis process',
                                               className="text-center"),
                                       
                                       dbc.Button(
            html.Span([html.I(className="far fa-file-alt ml-0"), " Report"]), href="https://drive.google.com/file/d/1DV-GhxB7kpaUtnh-crTKo4zWKl0hRrEw/view", target="_blank",
                                                  color="primary",
                                                  className="mt-3"), #LINK TO OUR REPORT

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5", justify="center"),

        html.A("Special thanks to Zett@Net",
               href="http://zetta-net.com/nuestros-servicios/", target="_blank"), #ZETTANET
        html.A(" and DS4A Colombia.",
               href="https://ds4a-colombia.correlation1.com/", target="_blank"), #DS4A
        html.A(" Glyphs from FontAwesome.",
               href="https://fontawesome.com/icons?m=free", target="_blank") #FONTAWESOME

    ])

])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)
