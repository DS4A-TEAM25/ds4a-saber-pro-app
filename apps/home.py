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
                            , style={'textAlign': 'center', 'background-image': 'url(/assets/banner.jpg)', 
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
                    , className="mb-5 mt-0 p-0")
        ]),

  
        dbc.Row([
            dbc.Col(html.H5(children='The \"Test on the Quality of Higher Education\" - SABER PRO – is administered to students who are about to complete their undergraduate education in Colombia.'
                            ' Social, demographic, financial, and geographic factors can affect student scores on the SABER PRO'
                                     )
                    , className="mb-4 mt-5")
           
            ]),
        
        dbc.Row([
            dbc.Col(html.H5(children='This app allows you to explore the factors that drive SABER PRO scores')
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='It consists of four main pages:' 
                            ' EXPLORE VARIABLES, allows you to explore how the SABER PRO scores vary according to different social, academic, regional, and financial student characteristics.' 
                           ' EXPLORE BY LOCATION, allows you to see scores by municipality or department and to compare them to other departments and municipalities in Colombia.'
                           ' EXPLORE BY UNIVERSITY, allows you to see scores by higher education institution and compare them to other institutions.'
                           ' MODELS, allows you to predict the scores if certain socioeconomic, relational, or educational variables changed.')
                    , className="mb-5")
        ]),

        

        dbc.Row([


            dbc.Col(dbc.Card(children=[html.H5(children='Access the code used to build this dashboard',
                                               className="text-center"),
                                       
                                       dbc.Button(
            html.Span([html.I(className="fab fa-github ml-0"), " GitHub"]), href="https://github.com/mparoca/ds4A-demo-app", target="_blank",
                                                  color="primary",
                                                  className="mt-3"),
 
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H5(children='Read about how we conducted our data analysis process',
                                               className="text-center"),
                                       
                                       dbc.Button(
            html.Span([html.I(className="far fa-file-alt ml-0"), " Report"]), href="#", target="_blank",
                                                  color="primary",
                                                  className="mt-3"),

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")
        ], className="mb-5", justify="center"),

        html.A("Special thanks to Zett@Net",
               href="http://zetta-net.com/nuestros-servicios/", target="_blank"), 
        html.A(" and DS4A Colombia.",
               href="https://ds4a-colombia.correlation1.com/", target="_blank"), 
        html.A(" Glyphs from FontAwesome.",
               href="https://fontawesome.com/icons?m=free", target="_blank")

    ])

])

# needed only if running this as a single page app
# if __name__ == '__main__':
#     app.run_server(host='127.0.0.1', debug=True)